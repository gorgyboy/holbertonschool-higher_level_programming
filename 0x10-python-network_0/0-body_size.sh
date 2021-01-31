#!/bin/bash
# Shows the size of the response from the server from a given url
curl -sI "$1" | grep Content-Length | cut -d " " -f2
