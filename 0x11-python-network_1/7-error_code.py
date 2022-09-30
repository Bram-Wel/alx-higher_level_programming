#!/usr/bin/python3
"""Fetches a url{requests package} and displays a header"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        resp = requests.get(argv[1])
        resp.raise_for_status()
        print(resp.text)
    except requests.exceptions.HTTPError:
        print("Error code:", resp.status_code)
