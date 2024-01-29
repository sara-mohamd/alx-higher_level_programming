#!/usr/bin/python3
"""A script which:
- accepts a URL,
- displays the value after sending a request to the URL
- of the X-Request-Id variable present in the respo's header.
- stores the email in the variable email
"""
import requests
import sys

if __name__ == "__main__":

    data_info = {"email": sys.argv[2]}
    requz = requests.post(sys.argv[1], data=data_info)
    print(requz.text)
