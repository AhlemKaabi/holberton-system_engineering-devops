#!/usr/bin/python3
""" API advanced """
import requests


def recurse(subreedit, hot_list=[], after=""):
    """
     Returns a list containing the titles
     of all hot articles for a given subreddit
    """
    URL_LINK = 'https://www.reddit.com'
    query = 'r/{}/hot.json'.format(subreedit)
    s1 = "Mozilla/5.0 (Linux; Android 11; Pixel 2;"
    s2 = "DuplexWeb-Google/1.0) AppleWebKit/537.36"
    s3 = "(KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36"
    agent = s1 + s2 + s3
    headers = {'User-agent': agent}
    params = {'after': after}
    r = requests.get(
        '{}/{}'.format(URL_LINK, query),
        allow_redirects=False,
        headers=headers,
        params=params
        )
    if r.status_code == 403 or r.status_code == 404:
        return
    data = r.json()
    after = data.get('data').get('after')
    posts = data.get('data').get('children')
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    if after:
        return recurse(subreedit, hot_list, after)
    return hot_list

if __name__ == '__main___':
    recurse(subreedit)
