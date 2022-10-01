#!/usr/bin/python3
"""Posts a variable to server"""
from sys import argv
import requests

if __name__ == "__main__":
    args = argv[:]
    if len(args) < 2:
        args.append("")
    datum = {'q': argc[1]}
    resp = requests.post('http://0.0.0.0:5000/search_user', data=datum)
    try:
        body = resp.json()
        if not body:
            print("No result")
        else:
            print(f"[{body.get('id')}] {body.get('name')}")
    except ValueError:
        if resp.status_code == 204:
            print("No result")
        else:
            print("Not a valid JSON")
