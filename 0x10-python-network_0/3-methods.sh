#!/bin/bash
# Shows the allowed methods for the given url
curl -sIX OPTIONS "$1" | grep Allow | cut -d " " -f2-
