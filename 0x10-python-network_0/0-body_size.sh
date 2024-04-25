#!/bin/bash

# Check if the user has provided a URL
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Fetch the response body and count its bytes
response_size=$(curl -s "$1" | wc -c)

# Display the size of the response body in bytes
echo "$response_size"
