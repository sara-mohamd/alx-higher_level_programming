#!/usr/bin/python3
"""A story script that
- accepts a URL
- a request is sent to the URL
- reveals the respo's body.
"""
import sys
import requests


if __name__ == "__main__":
    url_data = sys.argv[1]

    z = requests.get(url_data)
    if z.status_code >= 400:
        print("Error code: {}".format(z.status_code))
    else:
        print(z.text)
