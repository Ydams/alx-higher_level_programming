#!/bin/bash

# This sends a POST request to the passed URL, and then displays the body of the response

curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}"
