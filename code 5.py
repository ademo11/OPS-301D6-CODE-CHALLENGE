#!/usr/bin/env python3

# How to use Linux/Bash commands within Python
# First import the os library
import os

# Then use os.system to call any kind of bash command
var = "whoami" 
foo = "ip a"
baz = "lshw -short"
egg = "ls"
os.system(egg)
os.system(var)
os.system(foo)
os.system(baz)

# How to print to terminal

print("Welcome to Python!")

