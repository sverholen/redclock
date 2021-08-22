#!/bin/bash

# Generated at http://patorjk.com/software/taag/
cat << "EOF"
##############################################################################
##############################################################################
###                                                                        ###
###                                                                        ###
###                       _             _ _                                ###
###                      (_)_ __  _   _(_) |_ ___                          ###
###                      | | '_ \| | | | | __/ __|                         ###
###                      | | | | | |_| | | |_\__ \                         ###
###                      |_|_| |_|\__,_|_|\__|___/                         ###
###                                                                        ###
###                                                                        ###
##############################################################################
##############################################################################
EOF

# !!!
# Don't use this script when building dependencies for a docker
# Users can't be expected to have the necessary software installed to make
# the builds.
# For dockers: build everything inside the docker.
# Use this script when testing the app locally (development env).
# !!!

# DOCUMENTATION USED:
# https://python-poetry.org/docs/
# https://nanthony007.medium.com/stop-using-pip-use-poetry-instead-db7164f4fc72

# Using pip to install poetry avoids the need to pipe in dependencies in
# a docker when installing poetry there.
python -m pip install -U poetry
# To check if it is installed correctly: poetry -version

# Remove poetry.lock
if [[ -f "poetry.lock" ]]; then
    echo "Removing poetry.lock"
    rm poetry.lock
fi

# Run poetry init and setup basic information
poetry init

# Add project dependencies:
poetry add sqlalchemy
poetry add sqlalchemy-utils

# Let poetry download all packages and generate the poetry.lock file
poetry install

# Generate the requirements.txt
poetry export -f requirements.txt --output requirements.txt

