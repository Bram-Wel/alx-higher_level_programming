#!/bin/bash
# Passes custom header to server
curl -s "$1" -H "X-School-User-Id: 98"
