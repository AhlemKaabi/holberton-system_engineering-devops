#!/usr/bin/python3
""" API advanced """
import requests


def number_of_subscribers(subreedit):
    """
    Returns the number of suscriber for a given subreddit
    """
    URL_LINK = 'https://www.reddit.com'
    query = 'r/{}/about.json'.format(subreedit)
    s1 = "Mozilla/5.0 (Linux; Android 11; Pixel 2;"
    s2 = "DuplexWeb-Google/1.0) AppleWebKit/537.36"
    s3 = "(KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36"
    agent = s1 + s2 + s3
    headers = {'User-agent': agent}
    r = requests.get(
        '{}/{}'.format(URL_LINK, query),
        allow_redirects=False,
        headers=headers
        )
    if r.status_code == 403 or r.status_code == 404:
        return 0
    data = r.json()
    nb_s = data.get('data').get('subscribers')
    return nb_s

if __name__ == '__main___':
    number_of_subscribers(subreedit)