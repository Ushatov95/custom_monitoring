import psutil
import logging
import time
import json
import smtplib
import os

# Load the secrets file
with open('secrets.json') as f:
    secrets = json.load(f)

# Retrieve the email password
email_password = secrets['email']['password']
email_username = secrets['email']['username']
email_receiver_username = secrets['email']['receiver']

# Initialize the SMTP server connection parameters
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = email_username
smtp_password = email_password
sender_email = email_username
receiver_email = email_receiver_username

# Check for the existence of the file
filename = "error.log"
if not os.path.isfile(filename):
    # File doesn't exist, so create it
    with open(filename, 'w') as file:
        file.write("")

# Configure the logging module to write to a file
logging.basicConfig(filename='error.log', level=logging.ERROR)

# Initialize the error counts
cpu_error_count = 0
mem_error_count = 0

while True:
    # Get the CPU usage percentage
    cpu_percent = psutil.cpu_percent(interval=1)

    # Get the system memory usage statistics
    mem_stats = psutil.virtual_memory()

    # Calculate the percentage of used memory
    mem_percent_used = mem_stats.percent

    # Check if the CPU usage is too high
    if cpu_percent > 50:
        cpu_error_count += 1
        if cpu_error_count == 10:
            # Reset the error count
            cpu_error_count = 0
        # Log the error message to the file
        logging.error(f"CPU usage exceeds 50%: {cpu_percent}%")
        # Send an email notification
        message = 'Subject: CPU usage error\n\nThe CPU usage has exceeded 50% 10 times.\n\nPlease investigate.'
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message)

    # Check if the memory usage is too high
    if mem_percent_used > 50:
        mem_error_count += 1
        if mem_error_count == 10:
            # Reset the error count
            mem_error_count = 0
        # Log the error message to the file
        logging.error(f"Memory usage exceeds 50%: {mem_percent_used}%")
        # Send an email notification
        message = 'Subject: Memory usage error\n\nThe memory usage has exceeded 50% 10 times.\n\nPlease investigate.'
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message)

    # Wait for 20 seconds before checking again
    time.sleep(20)