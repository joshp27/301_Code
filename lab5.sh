#!/bin/bash
#Script: Ops 301 Class 05 Code Challenge
# Joshua Phipps
# 3/17/2023
# Purpose: Clearing Logs

#main
# COMPRESS CONTENTS TO BACK UP DIRECTORY
#Varibles
MakeLogFile (){
    source_path="/var/log/syslog"
    dest_path=$(pwd)
    source_path2="/var/log/wtmp"
    dest_path2=$(pwd)
    # Set filename to todays date
    filename=$(date +"%Y-%m-%d")
    filename2=$(date +"%Y-%m")
    #copy
    cp "$source_path" "$dest_path/$filename"
    cp "$source_path2" "$dest_path2/$filename2"
}
read -p "would you like to create a file log? 1 for yes, 2 for no, 3 to exit" Choice
#choice options
case $Choice in
    1)
        echo "File is created, continue to next part"
        MakeLogFile
        ;;
    2)
        echo "Continue to next part"
        ;;
    3)
        echo "now exiting"
        exit 0
        ;;
esac
clear
while true; do
# Prompt user for logfile
    read -p "Which log would you like to clear?" Logfile
#Var
    Filesize=$(stat -c%s "$Logfile")
    echo "size of $logfile = $Filesize bytes"
    read -p "Are you sure? 1 for Yes, 2 for no, 3 to exit" Choice
#choice options
    case $Choice in
        1)
            echo "Log is clear"
            :> $Logfile
            read -p "Enter to continue"
            ;;
        2)
            echo "Log was not clear"
            read -p "Enter to continue"
            ;;
        3)
            echo "now exiting"
            exit 0
            ;;
    esac
done