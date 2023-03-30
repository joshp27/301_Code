# # Script: Ops 301 Class 12 Code Challenge
# # Joshua Phipps
# # 3/28/2023
# # Purpose: Python Requests Library


#!/usr/bin/env python3

import requests

#main
import requests
# Prompt the user to type a string input as the variable for your destination URL.
user = input("Please enter a URL: ") or "https://www.google.com"
# Prompt the user to select a HTTP Method of the following options:
choices = {
    "1": "GET",
    "2": "POST",
    "3": "PATCH",
    "4": "DELETE",
    "5": "HEAD",
    "6": "TRACE",
    "7": "OPTIONS"
}
method_choice = input("Select one of the following: \n1) GET Request \n2) POST \n3) PATCH \n4) DELETE \n5) HEAD \n6) TRACE \n7) OPTIONS\n")
method = choices.get(method_choice)
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
print(f"The following {method} request is about to be sent to {user}:\n")
confirm = input("Do you want to continue? (y/n): ")
if confirm.lower() == "y":
    if method == "GET":
        reply = requests.get(user)
    elif method == "POST":
        reply = requests.post(user)
    elif method == "PATCH":
        reply = requests.put(user)
    elif method =="DELETE":
        reply =requests.delete(user)
    elif method == "HEAD":
        reply = requests.head(user)
    elif method == "TRACE":
        reply = requests.patch(user)
    elif method == "OPTIONS":
        reply = requests.options(user)
# Using the requests library, perform a GET request against your lab web server.
# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
status_code = {
    200: "okay",
    400: "Bad request",
    401: "Unauthorized",
    404: "Site not found",
}
if reply.status_code in status_code:
    print(f"Response status: {status_code[reply.status_code]}")
else:
    print(f"Response status: {reply.status_code}")
# For the given URL, print response header information to the screen.
print("Response Headers: ")
for header, value in reply.headers.items():
        print(f"{header}: {value}")
# end

