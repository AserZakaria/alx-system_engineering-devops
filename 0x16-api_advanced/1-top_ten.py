#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for request, limiting number of posts to 10
    params = {
        "limit": 10
    }

    # Send a GET request to subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if response status code indicates a not-found error (404)
    if response.status_code == 404:
        print("None")
        return

    # Parse JSON response and extract the 'data' section
    results = response.json().get("data")

    # Print titles of the top 10 hottest posts
    [print(c.get("data").get("title")) for c in results.get("children")]