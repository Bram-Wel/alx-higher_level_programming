#!/bin/bash
# Passes custom header to server
curl -H "X-Holberton-School-User-Id: 98" "$1"
