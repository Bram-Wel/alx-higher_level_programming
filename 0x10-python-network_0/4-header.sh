#!/bin/bash
# Passes custom header to server
curl -i -H "X-School-User-Id: 98" "$1"
