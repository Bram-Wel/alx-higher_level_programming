#!/usr/bin/python3
"""Fetches a url{requests package} and displays a header"""
import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.get(argv[1])
    print(resp.headers.get('X-Request-Id'))
