#!/bin/bash

# Hook to be run after project gen. Working dir is root of new project.
#
# cookiecutter has an issue with notify steps in drone
# (since they are also Jinja templates).
# Our hack is to not allow cookiecutter to template those
# steps and perform a post_gen_project join.

cat .drone_templateable.yml .drone_non_templateable.yml > .drone.yml
rm .drone_templateable.yml
rm .drone_non_templateable.yml
