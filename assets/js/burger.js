if (window.addEventListener)
{
    window.addEventListener('load', burger);
}
else
{
    window.attachEvent('onload', burger);
}

function burger()
{
    let stateful_elements = document.getElementsByClassName("stateful");

    for (let i = 0; i < stateful_elements.length; i++)
    {
        let dropdown = stateful_elements[i];
        let burger = document.getElementById(dropdown.getAttribute("for"));

        // get element dimensions (default to close state)
        dropdown.style.maxHeight = el_closed = 0;

        // get optional speed attribute
        speed = dropdown.getAttribute("speed");
        speed = speed ? speed : 400;
        
        // open/close nav
        burger.addEventListener('click', function (e)
        {
            if (dropdown.classList.contains('active'))
            {
                close(burger, dropdown);
            }
            else
            {
                open(burger, dropdown, speed);
            }
        });

        // try to setup auto-close functionality
        for (const navButton of dropdown.getElementsByClassName("auto-close"))
        {
            navButton.addEventListener('click', function (e)
            {
                close(burger, dropdown);
            });
        }
    }
};

function open(button, dropdown, speed)
{
    if (button) button.classList.add("active");
    dropdown.classList.add("active");

    open_height = dropdown.scrollHeight;

    // calculate animation duration from speed
    total_time = dropdown.scrollHeight / speed;
    dropdown.style.transition = "ease-in-out " + total_time + "s max-height";

    // set max height
    dropdown.style.maxHeight = dropdown.scrollHeight + "px";
}

function close(button, dropdown)
{
    if (button) button.classList.remove("active");
    dropdown.classList.remove("active");
    
    dropdown.style.maxHeight = 0;
}