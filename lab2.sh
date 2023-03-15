# Script: Ops 301 Class 02 Code Challenge
# Joshua Phipps
# 3/14/2023
# Purpose: Append; Date and Time


#!/bin/bash


# Copies /var/log/syslog to the current working directory
#current_date_time=$(date + "%Y-%m-%d_%H-%M-%S")
#echo >> "Current date and time: $current_date_time"


#Appends the current date and time to the filename
#echo "$(date) : $@" >> timefile.txt
#tail -n 1 timefile.txt



#!/bin/bash
current_date_time=$(date +"%Y-%m-%d_%H-%M-%S")
filename="syslog_$current_date_time"
cp /var/log/syslog "./$filename"

#Refrences (https://tecadmin.net/get-current-date-and-time-in-bash/)
#Refrences (https://www.google.com/search?q=append+bash+date+and+time+scirpt&rlz=1C1RAEH_enUS848US848&sxsrf=AJOqlzV2Vlo2o3YoGXiTWexK1WHVzeEqHw%3A1678836832507&ei=YAQRZMjDHoWK0PEPxci9gAc&ved=0ahUKEwjI86XIytz9AhUFBTQIHUVkD3AQ4dUDCBA&uact=5&oq=append+bash+date+and+time+scirpt&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQogQyBQgAEKIEMgUIABCiBDoKCAAQRxDWBBCwAzoHCCMQsAIQJzoICAAQCBAeEA06BQgAEIYDSgQIQRgAUOIJWMYSYJIcaAFwAXgAgAFoiAGZBZIBAzUuMpgBAKABAcgBCMABAQ&sclient=gws-wiz-serp#fpstate=ive&vld=cid:382d7cbb,vid:KczlrelRwXg)