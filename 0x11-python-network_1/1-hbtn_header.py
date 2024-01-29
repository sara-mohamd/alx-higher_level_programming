#!/usr/bin/python3
"""A script which::
- accepts a URL,
- makes a request  specified URL  shows  value of the X-Request-Id
- variable that may be found in the response's header.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url_data = sys.argv[1]

    request = urllib.request.Request(url_data)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
