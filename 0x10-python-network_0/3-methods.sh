#!/bin/bash
# Asks for server allowed Http methods
curl -sL -X "OPTIONS" "$1"
