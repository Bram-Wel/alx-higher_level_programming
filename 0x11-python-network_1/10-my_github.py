#!/usr/bin/python3
"""Displays github user id"""
import requests
from sys import argv

if __name__ == "__main__":
    session = requests.Session()
    session.auth = (argv[1], argv[2])
    resp = session.get('https://api.github.com/user')
    body = resp.json()
    try:
        if not body:
            print(None)
        else:
            print(body['id'])
    except KeyError:
        print(None)
