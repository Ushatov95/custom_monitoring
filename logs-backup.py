# Script is to be run as a cronjob once a day

import shutil
import os
import datetime

# Set the source and destination file paths
src_file = 'error.log'
dst_folder = 'logs'
dst_file = os.path.join(dst_folder, f'log_{datetime.date.today()}.txt')

# Create the backup folder if it doesn't exist
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)

# Copy the source file to the destination folder with the date appended to the file name
shutil.copy(src_file, dst_file)

# Wipe the contents of the source file
with open(src_file, 'w') as f:
    f.write('')