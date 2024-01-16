#!/usr/bin/python3

"""
returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Retrieve the hot posts from a subreddit recursively.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])
        for child in children:
            title = child.get("data", {}).get("title")
            hot_list.append(title)

        after = data.get("data", {}).get("after")
        if after:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
