#!/usr/bin/python3
"""
requests model
"""

if __name__ == '__main__':
    import requests
import urllib.request
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
