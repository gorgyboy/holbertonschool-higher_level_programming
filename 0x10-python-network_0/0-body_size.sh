#!/usr/bin/env bash
# Shows the size of the response from the server from a given url
curl -sw " %{size_download}" "$1" | cut -d " " -f3
