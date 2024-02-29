#!/bin/bash
# Sending a POST request with a custom header to cause the server to respond with the desired message
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: HolbertonSchool" -d "user_id=98"
