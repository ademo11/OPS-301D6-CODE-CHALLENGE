#!/bin/bash
# Script: OPS 301 Class 03 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 15 Mar 2023
# Purpose: Create a bash script that launches a menu system with the following options:
    # Hello world (prints “Hello world!” to the screen)
    # Ping self (pings this computer’s loopback address)
    # IP info (print the network adapter information for this computer)
    # Exit

echo "Please select an option:"
echo "1. Hello world"
echo "2. Ping self"
echo "3. IP info"
echo "4. Exit"

read choice

if [ "$choice" == "1" ]
then
    echo "Hello world!"
elif [ "$choice" == "2" ]
then
    ping 10.0.0.229
elif [ "$choice" == "3" ]
then
    ip a
elif [ "$choice" == "4" ]
then
    exit
else
    echo "Invalid choice"
fi
