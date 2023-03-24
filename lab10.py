# # Script: Ops 301 Class 10 Code Challenge
# # Joshua Phipps
# # 3/24/2023
# # Purpose: Python File Handling

#!/usr/bin/env python3


import os
# Create a new file if it does not exist
with open("X-Men.txt", "w") as x:
    # Append three lines
    x.write("Storm is the best \n")
    x.write("Storm is the weather Goddess \n")
    x.write("Winds heed my command!")
# Print the first line
with open("X-Men.txt", "r") as x:
    print(x.readline())
# Delete the file
os.remove("X-Men.txt")

# THIS IS WHAT I HAD AT FIRST
# import os
# # Create a new file if it does not exist
# x = open("X-Men.txt", "w")
# # Append three lines
# x = open("X-Men.txt", "a")
# x.write("Storm is the best \n")
# x.write("Storm is the weather Goddess \n")
# x.write("Winds heed my command!")
# # Print the first line
# x = open("X-Men.txt", "r")
# print(x.read(1))
# # Close a file when you're finished
# x = open("X-Men.txt", "r")
# print(x.readline())
# #Delete the file
# os.remove("X-Men.txt")
# # End




# # Create a new file if it does not exist
# x = open("X-Men.txt","w")

# # How to open a file
# x = open("X-Men.txt")

# # How to open a file and read it
# x = open("X-Men.txt", "r")
# print(x.read())

# # How to return the five first characters of a file
# x = open("X-Men.txt", "r")
# print(x.read(3))

# # # Close a file when you're finished
# # x = open("X-Men.txt", "r")
# # print(x.readline())
