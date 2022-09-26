#!/bin/bash
# Sends a post request to url
curl -s -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
