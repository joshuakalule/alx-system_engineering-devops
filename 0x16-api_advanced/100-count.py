#!/usr/bin/python3
"""
Parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords
    """
    app_name = '0x16-api_advanced'
    user_name = 'FeelingPsychology300'
    headers = {'User-Agent': f'{app_name}/0.0.1 by /u/{user_name}'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data')
    after = data.get('after')
    children = data.get('children')

    for child in children:
        title = child.get('data').get('title')
        for word in word_list:
            if word.lower() in title.lower():
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    if after is not None:
        return count_words(subreddit, word_list, word_count, after)

    if not word_count:
        return

    for key, value in sorted(word_count.items(),
                             key=lambda item: item[1], reverse=True):
        print('{}: {}'.format(key, value))
