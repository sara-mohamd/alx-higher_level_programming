#!/usr/bin/python3
""" 3-error_code """

import urllib.request


if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from sys import argv

    try:
        with urlopen(argv[1]) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
