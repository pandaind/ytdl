#!/bin/bash

source venv/bin/activate

# Ask for user input
read -p "Enter the YouTube video or playlist URL: " url
read -p "Enter the download path (default is 'downloads'): " download_path

# Provide a default download path if none is provided
if [ -z "$download_path" ]; then
  download_path="downloads"
fi

# Run the Python script with user inputs
echo "Starting the download process..."
python youtube_downloader.py "$url" "$download_path"

echo "Download process complete."
