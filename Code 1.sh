#!/bin/bash

# Get current date and time in the format YYYY-MM-DD-HH-MM-SS
timestamp=$(date +%Y-%m-%d-%H-%M-%S)

# Set the filename with timestamp
filename="syslog-$timestamp.log"

# Copy the syslog file to the current working directory with the new filename
cp /var/log/syslog $filename


echo "Copied /var/log/syslog to $filename"

# Reference
OpenAI

# breakdown of the code The date command is used to get the current date and time in the format YYYY-MM-DD-HH-MM-SS.
 # The filename is set with the timestamp by using the variable $timestamp.
 # The cp command is used to copy the syslog file to the current working directory with the new filename.
 # A message is printed to confirm that the file has been copied.
