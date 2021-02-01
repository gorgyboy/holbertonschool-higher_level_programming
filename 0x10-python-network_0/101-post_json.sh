#!/bin/bash
# Sends a JSON POST request to an URL and displays the body of the response
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
