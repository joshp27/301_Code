#!/bin/bash
#Script: Ops 301 Class 04 Code Challenge
# Joshua Phipps
# 3/15/2023
# Purpose: Conditionals in Menu Systems


hello_world() {
    echo "Hello World"
}

ping_local() {
    ping -c4 127.0.0.1 $$
}

ipinfo() {
    ip a
} 

Exit() {
    return
} 
echo "1- Hello World";
echo "2- Ping";
echo "3- ipinfo";
echo "4- Exit"
echo "Make Selection 1,2,3 or 4"
read selection

if [[ $selection == 1 ]]; then
    hello_world
elif [[ $selection == 2 ]]; then
    ping_local
fi
if [[ $selection == 3 ]]; then
    ipinfo
elif [[ $selection == 4 ]]; then
    Exit 

fi

#End