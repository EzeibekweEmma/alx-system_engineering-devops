#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers (not
active users, total subscribers) for a given subreddit. If an invalid subreddit
is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, allow_redirects=False, headers={
                            "User-Agent": "Nico@alx/1.0"})
    if response.status_code != 200:
        return 0
    else:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
