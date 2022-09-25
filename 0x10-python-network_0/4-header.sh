#!/bin/bash
# Passes custom header to server
curl -s "$1" -H "X-HolbertonSchool-User-Id:: 98"
