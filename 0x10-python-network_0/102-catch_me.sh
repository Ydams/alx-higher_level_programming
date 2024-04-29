#!/bin/bash
# This is a script that makes a request to cause the server to respond in a  specific way containing You got me!
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"

