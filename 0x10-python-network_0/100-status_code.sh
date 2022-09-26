#!/bin/bash
# Displays the status code of Http response
curl -sI "$1"| grep "HTTP" | cut -d " " -f 2
