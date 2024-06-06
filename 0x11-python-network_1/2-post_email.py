#!/usr/bin/python3
""" Python script that fetches URL """
if __name__ == '__main__':
    from urllib.request import urlopen
    from urllib.parse import urlencode
    from sys import argv

    value = {"email": argv[2]}
    with urlopen(f'{argv[1]}', {urlencode(value).encode("ascii")}) as resp:
        head = resp.headers.get('X-Request-Id')
        print(resp.read().decode('utf-8'))
