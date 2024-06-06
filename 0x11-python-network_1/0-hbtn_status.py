#!/usr/bin/python3
""" Python script that fetches URL """

if __name__ == '__main__':
    import urllib.request as ur

    with ur.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        f = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(f)))
        print("\t- content: {}".format(f))
        print("\t- utf8 content: {}".format(f.decode('utf-8')))
