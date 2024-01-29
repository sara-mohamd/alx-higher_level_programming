#!/usr/bin/python3
"""A script which:
- accepts a URL,
- a request is sent to the URL
- shows the response's body (decoded in utf-8).
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error
    try:
        with request.urlopen(sys.argv[1]) as respo:
            print(respo.read().decode('UTF-8'))
    except error.HTTPError as erdz:
        print('Error code:', erdz.code)
