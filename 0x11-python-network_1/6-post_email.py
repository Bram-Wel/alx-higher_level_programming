#!/usr/bin/python3
"""Fetches a url{requests package} and displays a header"""
import requests
from sys import argv

if __name__ == "__main__":
    datum = {'email': argv[2]}
    resp = requests.post(argv[1], data=datum)
    print(resp.text)
