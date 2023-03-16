#!/bin/bash
# Script: OPS 301 Class 03 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 15 Mar 2023
# Purpose: Create a new bash script that performs the following:

# Prompt user for input directory path
read -p "OZONE: " directory

# Prompt user for input permissions number
while true; do
  read -p "Enter permissions number: " permissions
  if [[ "$permissions" =~ ^[0-9]+$ ]]; then
    break
  else
    echo "Invalid input. Please enter a number."
  fi
done

# Navigate to input directory and change file permissions

# Prompt user for input directory path
read -p "Enter directory path: " directory

# Prompt user for input permissions number
read -p "Enter permissions number: " permissions

# Navigate to input directory and change file permissions
cd "$directory"
chmod -R "$permissions" .

# Print directory contents and new permissions
echo "Directory contents:"
ls -l


# References
 # OpenAI