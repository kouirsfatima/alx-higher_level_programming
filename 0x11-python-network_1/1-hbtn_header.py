#!/usr/bin/python3
"""A script that:
- sends a request to the URL and displays the value
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
     print dict(req.headers).get("X-Request-Id")
