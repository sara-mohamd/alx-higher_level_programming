#!/bin/bash
# Delete request to the URL passed as the first argument and displays the body of the response
curl -sXL DELETE "$1"
