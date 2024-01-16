#!/usr/bin/python3
"""
Module to query the Reddit API and returns the number of subscribers
"""


import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    heads = {'User-Agent': 'Custom User Agent'}
    res = requests.get(url, headers=heads)
    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    return 0
