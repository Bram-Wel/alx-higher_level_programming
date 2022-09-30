#!/bin/bash
# Displays the status code of Http response
curl -s -o /dev/null -w "%{http_code}" "$1"
