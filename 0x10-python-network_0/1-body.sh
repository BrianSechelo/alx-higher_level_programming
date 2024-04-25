#!/bin/bash

# Check if the user has provided a URL
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the provided URL and display the body of the response
response_body=$(curl -s -o /dev/null -w "%{http_code}" "$1" | { 
    read status_code
    if [ $status_code -eq 200 ]; then
        curl -s "$1"
    fi
})

# Display the body of the response (if status code was 200)
echo "$response_body"
