#!/bin/bash
# Passes custom header to server
curl -s -H "X-School-User-Id: 98" "$1"
