#!/usr/bin/python3
"""return list of titles for hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles
    for a given subreddit
    """
    app_name = '0x16-api_advanced'
    user_name = 'FeelingPsychology300'
    headers = {'User-Agent': f'{app_name}/0.0.1 by /u/{user_name}'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    after = data.get('after')
    children = data.get('children')

    for child in children:
        hot_list.append(child.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
