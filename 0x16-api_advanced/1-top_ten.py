#!/usr/bin/python3
""" API advanced """
import requests


def top_ten(subreedit):
    """
    Returns top 10 posts in a subreedit
    """
    url = 'https://www.reddit.com'
    query_string = 'r/{}/hot.json'.format(subreedit)
    s1 = "Mozilla/5.0 (Linux; Android 11; Pixel 2;"
    s2 = "DuplexWeb-Google/1.0) AppleWebKit/537.36"
    s3 = "(KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36"
    agent = s1 + s2 + s3
    # print(agent)
    headers = {'User-agent': agent}
    params = {'limit': 10}
    r = requests.get(
        '{}/{}'.format(url, query_string),
        allow_redirects=False,
        headers=headers,
        params=params
        )
    if r.status_code == 403 or r.status_code == 404:
        print('None')
        return
    data = r.json()
    posts = data.get('data').get('children')
    for post in posts:
        print(post.get('data').get('title'))
    return

if __name__ == '__main___':
    top_ten(subreedit)
