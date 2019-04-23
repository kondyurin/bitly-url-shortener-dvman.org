import os
import argparse
import requests
from dotenv import load_dotenv


def get_shorten_url(token, url):
    """Return bitlink from url"""
    payload = {
        'long_url': url
    }
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(url, headers=headers, json=payload)
    if not response.ok:
        return
    data = response.json()
    shorten_url = data['link']
    return shorten_url


def get_url_clicks(shorten_url):
    """Return bitlink clicks count"""
    params = {
        'units': -1,
        'unit': 'day'
    }
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(shorten_url)
    response = requests.get(url, headers=headers, params=params)
    if not response.ok:
        return
    data = response.json()
    total_clicks = data['total_clicks']
    return total_clicks


def is_bitlink(url):
    """Return True if url is bitlink"""
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url)
    response = requests.get(url, headers=headers)
    if not response.ok:
        return
    return response.ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    input_url = args.url
    load_dotenv()
    token = os.getenv("TOKEN")
    url_domain = input_url.split('//')[1]
    if is_bitlink(url_domain):
        total_clicks = get_url_clicks(url_domain)
        print(total_clicks)
    else:
        shorten_url = get_shorten_url(token, input_url)
        print(shorten_url)