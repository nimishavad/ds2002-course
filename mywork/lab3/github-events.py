#!/usr/bin/env python3

import os
import json
import requests

# Get GitHub username from environment variable
GHUSER = os.getenv('GITHUB_USER')

if not GHUSER:
    print("Error: GITHUB_USER environment variable not set.")
    exit(1)

# Construct API URL
url = f'https://api.github.com/users/{GHUSER}/events'

# Make request
response = requests.get(url)

if response.status_code != 200:
    print("Error fetching data from GitHub API")
    exit(1)

# Load JSON data
r = json.loads(response.text)

# Print first 5 events
for x in r[:5]:
    event = x['type'] + ' :: ' + x['repo']['name']
    print(event)

