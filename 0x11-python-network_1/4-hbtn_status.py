#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
if __name__ == "__main__":
    from requests import get

    file = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(file.text.__class__))
    print("\t- content: {}".format(file.text))
