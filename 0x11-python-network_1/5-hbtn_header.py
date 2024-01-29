#!/usr/bin/python3
"""displays a request's X-Request-Id header variable for a certain URL.
"""
import sys
import requests


if __name__ == "__main__":
    url_data = sys.argv[1]

    z = requests.get(url_data)
    print(z.headers.get("X-Request-Id"))
