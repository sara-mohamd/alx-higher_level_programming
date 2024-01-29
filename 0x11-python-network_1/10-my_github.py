#!/usr/bin/python3
"""A is scripted which:
- takes your username and password for GitHub.
- displays your ID using the GitHub API.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authenti = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    x = requests.get("https://api.github.com/user", auth=authenti)
    print(x.json().get("id"))
