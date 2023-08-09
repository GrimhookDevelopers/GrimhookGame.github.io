# Grimhook Website

The offical site can be accessed on https://grimhook.com

# Setup

This site is built with Jekyll see their setup instructions to get started: https://jekyllrb.com/docs/step-by-step/01-setup/

If you already have ruby setup follow these steps:

1. run `gem install jekyll bundler` (can be run in any directory)
2. run `bundle install` at the root of the project
3. run `bundle exec jekyll serve` to preview the site at http://localhost:4000/

## Updating Team Members

### `_data/team.yml`

List of project members shown in the team section.

A member's portrait is required but the link and link-name are optional.

### `_source/team-portraits`

Portraits should have an aspect ratio of 4:5 and have a width of at least 512px. If a portrait is added or modified make sure to run the the optimization script.

### Optimization Script

`py ./optimize_portraits.py` may be run to generate optimized images and the `-force` can also be provided to ensure no images are skipped.