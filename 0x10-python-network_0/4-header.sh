#!/bin/bash
# Sends a custom header to the given url and shows the response
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
