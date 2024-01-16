#!/usr/bin/python3

"""
Module to query the Reddit API and return the number
of subscribers
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number
    of subscribers
    for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
        )

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
