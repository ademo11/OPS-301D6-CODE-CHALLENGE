#!/bin/bash
# Script: OPS 301 Class 03 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 17 Mar 2023
# Purpose: Print to the screen the file size of the log files before compression
 # Compress the contents of the log files listed below to a backup directory
 # The file name should contain a time stamp with the following format 
 # Clear the contents of the log file
 # Print to screen the file size of the compressed file
 # Compare the size of the compressed files to the size of the original log files

backup_dir="Backups"
mkdir -p "$backup_dir"
timestamp=$(date +%Y%m%d%H%M%S)

for file in "ademo.txt"
do
  original_size=$(du -sh "$file" | cut -f1)
  echo "Original file size of $file: $original_size"

  compressed_file="$backup_dir/$(basename $file)-$timestamp.zip"
  zip -qj "$compressed_file" "$file"

  truncate -s 0 "$file"

  compressed_size=$(du -sh "$compressed_file" | cut -f1)
  echo "Compressed file size of $compressed_file: $compressed_size"

  if [[ "$compressed_size" < "$original_size" ]]; then
    echo "Compression successful, saved $(echo "$original_size - $compressed_size" | bc -l) in disk space."
  else
    echo "Compression failed or didn't save disk space."
  fi
done

# Reference
Open source
