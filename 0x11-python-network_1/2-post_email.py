#!/usr/bin/python3
"""A script which:
- accepts a URL
- a POST request is sent to the supplied URL
- accepts an email parameter
- shows the response's body in brackets
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    resource = sys.argv[1]
    val = {"email": sys.argv[2]}
    content_data = urllib.parse.urlencode(val).encode("ascii")
    requ = urllib.request.Request(resource, content_data)
    with urllib.request.urlopen(requ) as resp:
        print(resp.read().decode("utf-8"))
