#!/bin/bash
# Sends a POST request to to the given url and shows the response
curl -sX POST -F "email=hr@holbertonschool.com" -F "subject=I will always be here for PLD" "$1"
