#!/usr/bin/python3
"""a GitHub repository's 10 most recent commits are listed.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2],
        sys.argv[1])

    n = requests.get(url)
    commits = n.json()

    try:
        for z in range(10):
            print("{}: {}".format(
                commits[z].get("sha"),
                commits[z].get("commit").get("author").get("name")))
    except IndexError:
        pass
