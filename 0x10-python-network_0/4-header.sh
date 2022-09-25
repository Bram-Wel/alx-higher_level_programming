#!/bin/bash
# Passes custom header to server
curl -sL -H "X-School-User-Id:98" "$1"
