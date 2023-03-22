# Script: Ops 301 Class 07 Code Challenge
# Joshua Phipps
# 3/21/2023
# Purpose: Append; Directory Creation

import os
# Declare function
def generate_directory_structure(path):
    for (root, dirs, files) in os.walk(path):
        print("Root directory:", root)
        print("Sub-directories:", dirs)
        print("Files:", files)
# Get user input
path = input("Enter directory path: ")
# Call function with user input as argument
generate_directory_structure(path)