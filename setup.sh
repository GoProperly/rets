#!/usr/bin/env bash

# Create a virtual environment and install python dependencies
if [ ! -d "venv" ]; then
    python3.6 -m venv venv
fi

# Turn on the virtual environment
source venv/bin/activate

# Install dependencies
python3.6 setup.py -q install
