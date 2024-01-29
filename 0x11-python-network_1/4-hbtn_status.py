#!/usr/bin/python3
"""fetches is https://intranet.hbtn.io/status."""

import requests
if __name__ == "__main__":
    requz = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(requz.text)}")
    print(f"\t- content: {requz.text}")
