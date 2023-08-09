#!/usr/bin/env python
#SETMODE 777

#----------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------ HEADER --#

"""
:author:
    Nick Maclean

:synopsis:
    Script for generating optimzed images.

:description:
    This script can be run as-is. Make sure to install the Pillow python module first though.
    The -force flag may be provided to prevent skipping images.
"""

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- IMPORTS --#

# Built-in
import inspect
import os
import sys
from typing import Callable

# Third party
try:
    from PIL import Image
except ModuleNotFoundError:
    print("The pillow module is a required dependency. Run 'pip install pillow', then try to run this file again.")
    sys.exit()

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- GLOBALS --#

verbose = True
supported_image_extensions = ["png", "gif", "jpg", "jpeg"]

#----------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------- FUNCTIONS --#


def _log(label: str, message: str, indent: str, caller):
    caller_file = caller.f_back.f_code.co_filename
    caller_line = caller.f_back.f_lineno
    caller_name = caller.f_back.f_code.co_name

    print(f"{label}: {message}")
    print(f"{indent}  {caller_name}(): Line number {caller_line}")
    print(f"{indent}  File {caller_file}")


def log_message(message: str): _log("INFO", message, "    ", inspect.currentframe().f_back)
def log_warning(message: str): _log("WARNING", message, "       ", inspect.currentframe().f_back)
def log_error(message: str): _log("ERROR", message, "     ", inspect.currentframe().f_back)


def iterate_through_files(directory: str, callback: Callable[[str, str], None], ext: str = None, **kwargs) -> int:
    """
    Recursively search files under the directory and performs the callback on each file.

    :param directory: parent directory to search underneath
    :param callback: function performed on each file
    :param ext: all files must have this extension to be considered
    :return: number of files successfully iterated
    :type: int
    """
    if not os.path.isdir(directory):
        log_error(f"Provided directory is not valid: {directory}")
        return None

    count = 0
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            # apply extension filter, if provided
            if ext:
                if isinstance(ext, str):
                    ext = [ext]

                found = False
                for ex in ext:
                    if file.lower().endswith(ex):
                        found = True
                        break
                if not found:
                    continue

            try:
                callback(root, file, **kwargs)
            except Exception as e:
                log_error(e)
                continue

            count += 1

    return count


def update_image_resolution(input_image_path: str, output_image_path: str, output_resolution: tuple[int, int]) -> bool:
    """
    Creates a copy of the input image with a new resolution.

    :param input_image_path:
    :param output_image_path:
    :param output_resolution:
    :return: success
    """
    if not os.path.isfile(input_image_path):
        log_error(f"Provided input path is not valid: {input_image_path}")
        return None

    image = Image.open(input_image_path)
    image.thumbnail(output_resolution)

    try:
        image.save(output_image_path, progressive=True, quality=100)
    except OSError:
        log_error(f"Unable to write to path: {output_image_path}")
        return None

    return True


def optimize_team_portrait(directory: str, file_name: str, **kwargs):
    # validate kwargs
    if kwargs is None or 'dir_out' not in kwargs:
        log_error("This method requires the 'dir_out' argument in kwargs")
        return None

    # build/validate input path
    file_input = os.path.join(directory, file_name)
    if not os.path.isfile(file_input):
        log_error(f"Provided file could not be found: {file_input}")
        return None

    # create output path
    file_input_name = os.path.splitext(os.path.basename(file_input))[0]
    file_output_name = f"{file_input_name}.png"
    file_output = os.path.join(kwargs['dir_out'], file_output_name)

    # this portrait has been optimized
    # skip it
    if ('force' not in kwargs or not kwargs['force']) and os.path.isfile(file_output):
        if os.path.getmtime(file_output) > os.path.getmtime(file_input):
            if verbose:
                log_message(f"{file_input_name} has already been optimized")
            return True

    # create optimized image
    output_resolution = (512, 640)
    result = update_image_resolution(file_input, file_output, output_resolution)

    if verbose:
        log_message(
            f"Optimized {file_input_name}; output to {file_output}"
            if result else
            f"Failed to optimize {file_input_name}; output to {file_output}"
        )

    return result


def optimize_team_portraits(force=False):
    dir_current = os.path.abspath(os.getcwd())
    dir_src = os.path.join(dir_current, "_source", "team-portraits")
    dir_out = os.path.join(dir_current, "assets", "images", "team")

    if verbose:
        log_message(f"Portraits from {dir_src} will be optimized into {dir_out}")

    files_found = iterate_through_files(dir_src, optimize_team_portrait, supported_image_extensions, dir_out=dir_out, force=force)

    if verbose:
        log_message(f"Attempted to optimze {files_found} file(s)")


#----------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------- MAIN --#


def main():
    force = '-force' in sys.argv
    optimize_team_portraits(force)


if __name__ == '__main__':
    main()
