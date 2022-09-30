#!/usr/bin/python3
"""Post request with headers"""
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import HTTPError

if __name__ == "__main__":
    req = Request(argv[1])
    try:
        with urlopen(req) as resp:
            body = resp.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print("Error code:", e.code)
