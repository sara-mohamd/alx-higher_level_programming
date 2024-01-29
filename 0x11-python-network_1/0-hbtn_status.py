#!/usr/bin/python3
"""a text that script
- fetches https://alx-intranet.hbtn.io/status.
- uses the package urlib
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        content_data = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(content_data)))
        print("\t- content: {}".format(content_data))
        print("\t- utf8 content: {}".format(content_data.decode('utf-8')))
