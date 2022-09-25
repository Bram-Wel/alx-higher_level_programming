#!/bin/bash
#Scripts takes a url, sends a req msg to it & shows response body size 
curl -s "$1" | wc -c
