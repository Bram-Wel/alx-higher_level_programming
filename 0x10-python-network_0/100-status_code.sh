#!/bin/bash
# Displays the status code of Http response
curl -o /dev/null -sw "%{http_code}\n" "$1"
