#!/usr/bin/python3
"""Queries the Reddit API."""
import requests
import json


def top_ten(subreddit):
    """Get nfirst 10 hot posts of a subreddit."""
    url = 'https://www.reddit.com/api/search_reddit_names.json'
    user_agent = 'web:BrUtzve5P9cP8IZB8eCasA:v1 (by /u/Fantastic_Payment420)'
    headers = {
        'User-Agent': user_agent
    }
    params = {
        'query': subreddit
    }
    resp = requests.get(
        url, headers=headers, allow_redirects=False, params=params
    )
    found = resp.json()
    if subreddit not in found['names']:
        print(None)

    sub_url = f'https://www.reddit.com/r/{subreddit}.json'
    sub_resp = requests.get(
        sub_url, headers=headers, allow_redirects=False
    )

    if sub_resp.status_code != 200:
        print(None)
    data = sub_resp.json()
    # print(json.dumps(data))

    for n, post in enumerate(data['data']['children']):
        if n >= 10:
            break
        print(post['data']['title'])
