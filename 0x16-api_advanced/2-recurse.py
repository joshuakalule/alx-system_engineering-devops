#!/usr/bin/python3
"""return list of titles for hot articles"""
import json
import requests
import sys


def recurse(subreddit, pop_list=[], after=None):
    """return hot article titles"""

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    params = {
        'exact': True,
        'query': subreddit
    }

    verify = requests.get(
        'https://www.reddit.com/api/search_reddit_names.json',
        headers=headers, params=params)

    if 'error' in verify.json().keys():
        return None

    params = {
        'after': after
    }

    rObj = requests.get('https://www.reddit.com/r/' + subreddit + '.json',
                        headers=headers, params=params)

    for listi in rObj.json()['data']['children']:
        pop_list.append(listi['data']['title'])

    if rObj.json()['data']['after'] is None:
        return pop_list

    return recurse(subreddit, pop_list, rObj.json()['data']['after'])
