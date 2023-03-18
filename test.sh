#!/bin/bash

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