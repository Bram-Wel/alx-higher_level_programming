#!/usr/bin/python3
"""Post request with headers"""
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == "__main__":
    data = {'email': argv[2]}
    data = urlencode(data)
    data = data.encode('ascii')
    req = Request(argv[1], data)
    with urlopen(req) as resp:
        body = resp.read().decode('utf-8')
    print(body)
