#!/bin/bash

python -m venv venv

source venv/bin/activate

# Install required Python packages
echo "Installing required Python packages..."
pip install -r requirements.txt

