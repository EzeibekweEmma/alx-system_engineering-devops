#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the first 10 
hot posts listed for a given subreddit"""
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
