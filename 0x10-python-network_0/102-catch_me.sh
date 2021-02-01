#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me to get respond "You got me!"
curl -sL -X PUT -F "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
