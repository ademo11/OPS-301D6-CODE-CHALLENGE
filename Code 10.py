#!/usr/bin/env python3
# Script: OPS 301 Class 03 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 24 Mar 2023
# Purpose: Open a new file in write mode

file = open("LAB10.txt", "w")

# Append three lines to the file
  
file.write("Africa is a continent. This is line 1\n")
file.write("Nigeria is from West Africa. This is line 2\n")
file.write("Crude Oil is the major Resources. This is line 3\n")


# Close the file
file.close()

# Open the file in read mode
file = open("LAB10.txt", "r")

# Read the first line and print it to the screen
first_line = file.readline()
print(first_line)

# Close the file
file.close()

# Delete the file
import os
os.remove("LAB10.txt")


# End
