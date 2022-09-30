#!/usr/bin/python3
"""Fetches and displays value for header X-Request-Id from passed url"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        headers = resp.info()
    print(headers['X-Request-Id'])
