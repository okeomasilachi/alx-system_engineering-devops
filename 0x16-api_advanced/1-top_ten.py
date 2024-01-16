#!/usr/bin/python3

"""
Module to query the Reddit API and returns the number
of subscribers
"""


import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "okeoma"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        post = data["data"]["children"]
        [print(f"{post['data']['title']}") for i, post in enumerate(post[:9])]
    else:
        print("None")
