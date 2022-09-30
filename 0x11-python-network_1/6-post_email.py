#!/usr/bin/python3
"""Fetches a url{requests package} and displays a header"""
import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.post(argv[1])
    print(resp.headers['X-Request-Id'])
