#!/usr/bin/python3
"""Fetches a url using requests package/module"""
import requests

if __name__ == "__main__":
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(resp.text)}")
    print(f"\t- content: {resp.text}")
