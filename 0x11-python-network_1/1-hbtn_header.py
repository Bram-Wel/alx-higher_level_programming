#!/usr/bin/python3
"""Fetches and displays value for header X-Request-Id
from passed url"""
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen(sys.argv[1]) as resp:
        headers = resp.info()
    print(headers['X-Request-Id'])
