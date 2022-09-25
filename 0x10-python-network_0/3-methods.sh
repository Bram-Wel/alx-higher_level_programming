#!/bin/bash
# Asks for server allowed Http methods
curl -sLI -X "OPTIONS" "$1" | grep "Allow" | cut -b 8-
