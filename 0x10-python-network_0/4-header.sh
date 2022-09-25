#!/bin/bash
# Passes custom header to server
curl -s -X GET -H "X-School-User-Id: 98" "$1"
