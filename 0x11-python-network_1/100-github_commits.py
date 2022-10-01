#!/usr/bin/python3
"""prints 10 github repo commits in order(From most recent)"""
import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.get("https://api.github.com/repos/"
                        + argv[2] + "/" + argv[1] + "/commits")
    body = resp.json()
    try:
        for i in range(10):
            print(f"{body[i].get('sha')}:\
 {body[i].get('commit').get('author').get('name')}")
    except IndexError:
        pass
