#!/bin/bash
# Send a JSON POST req and concatenate filename to it
curl -sH "Content-Type: application/json" -d @"$2" "$1"
