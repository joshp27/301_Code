#!/bin/bash
#Script: Ops 301 Class 02 Code Challenge
# Joshua Phipps
# 3/15/2023
# Purpose: File Permissions


#Prompts user for input directory path.
read -p "Type in the directory path you would like to edit permissions on?" Directory
#Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
read -p "Type the command code to change the permissions" Code
#Navigates to the directory input by the user and changes all files inside it to the input setting.
ls -l "$Directory"
#Prints to the screen the directory contents and the new permissions settings of everything in the directory.
chmod -R "$Code" "$Directory"

echo "Permissions for directory and its contents have been updated successfully" 

# end 