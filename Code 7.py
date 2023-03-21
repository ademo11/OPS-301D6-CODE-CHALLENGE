#!/usr/bin/env python3
# Script: OPS 301 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 21 Mar 2023
# Purpose: Import libraries

import os

def generate_directories_files(path):
    for root, directories, files in os.walk(path):
        # Print the current root directory
        print(root)
        
        # Print all subdirectories in the current directory
        for directory in directories:
            print(os.path.join(root, directory))
        
        # Print all files in the current directory
        for file in files:
            print(os.path.join(root, file))

# Ask the user for a file path
path = input("Enter the file path: ")

# Call the function to generate directories and files
generate_directories_files(path)
