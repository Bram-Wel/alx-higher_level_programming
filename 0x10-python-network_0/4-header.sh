#!/bin/bash
# Passes custom header to server
curl -H "X-School-User-Id: 98" "$1"
