#!/usr/bin/python3
"""Queries the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Get number of subs."""
    user_agent = 'web:BrUtzve5P9cP8IZB8eCasA:v1 (by /u/Fantastic_Payment420)'
    headers = {
        'User-Agent': user_agent
    }
    params = {
        'query': subreddit
    }

    sub_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    sub_resp = requests.get(
        sub_url, headers=headers, allow_redirects=False
    )

    if sub_resp.status_code != 200:
        return 0
    data = sub_resp.json()
    # print(json.dumps(data))
    subscribers = int(data['data']['subscribers'])
    return subscribers
