#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -su -H -L POST "email=test@gmail.com&subject=I%will%always%be%here%for%PLD" $1
