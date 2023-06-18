#!/bin/bash

# Set the source and destination file paths
src_file="error.log"
dst_folder="logs"
dst_file="$dst_folder/log_$(date +'%Y-%m-%d').txt"

# Create the backup folder if it doesn't exist
if [ ! -d "$dst_folder" ]; then
  mkdir "$dst_folder"
fi

# Copy the source file to the destination folder with the date appended to the file name
cp "$src_file" "$dst_file"

# Wipe the contents of the source file
> "$src_file"
