#!/usr/bin/env python3
# Script: OPS 301 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 21 Mar 2023
# Purpose: How to create and print a list

my_list = ["apple", "banana", "kunu", "guava", "plaintain", "date", "agbado", "Alkaline water", "jollof", "ogi"]
print(my_list)

# How to print the first item only

my_list = ["apple", "banana", "kunu", "guava", "plaintain", "date", "agbado", "Alkaline water", "jollof", "ogi"]
print(my_list [0]) 

# Print the fourth element of the list

my_list = ["apple", "banana", "kunu", "guava", "plaintain", "date", "agbado", "Alkaline water", "jollof", "ogi"]
print(my_list [3])

# Print the sixth through tenth element of the list

my_list = ["apple", "banana", "kunu", "guava", "plaintain", "date", "agbado", "Alkaline water", "jollof", "ogi"]
print(my_list [5:9])

# Change the value of the seventh element to "onion"

my_list = ["apple", "banana", "kunu", "guava", "plaintain", "date", "agbado", "Alkaline water", "jollof", "ogi"]
my_list[6] = "onion"
print("Updated list:", my_list)

# How to print the last item only by counting backwards

my_list = ["apple", "banana", "kunu", "guava", "plaintain", "date", "agbado", "Alkaline water", "jollof", "ogi"]
print(my_list [-1])

# How to print a range of elements in a list

my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(my_list[2:5])


# How to add an item to a list

my_list = ["apple", "banana", "cherry"]
my_list.append("orange")
print(my_list)

