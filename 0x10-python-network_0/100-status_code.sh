#!/bin/bash
# Displays only the status code of the response for the given url
curl -sw "${response_code}\n" "$1" -o /dev/null
