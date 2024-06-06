#!/usr/bin/python3
"""
  - sends a request to the URL
  - displays the value of the X-Request-Id variable
  found in the header of the response.
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    with urlopen(f'{argv[1]}') as resp:
        head = resp.headers.get('X-Request-Id')
        print(head)
