#!/usr/bin/python3
"""A script which:
- accepts a query
- sends make POST research request to http://0.0.0.0:5000/search_user
as a parameter, using the query.
"""
import sys
import requests


if __name__ == "__main__":
    query = "" if len(sys.argv) == 1 else sys.argv[1]
    post_data = {"q": query}

    z = requests.post("http://0.0.0.0:5000/search_user", data=post_data)
    try:
        res = z.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
