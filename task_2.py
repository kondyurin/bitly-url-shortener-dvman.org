import os
import requests
from dotenv import load_dotenv


def get_shorten_url(token, url):
    """
    Ф-ия принимает токен, url
    Ф-ия возвращает битлинк
    """
    payload = {
        'long_url': url
    }
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(url, headers=headers, json=payload)
    if response.ok:
        data = response.json()
        shorten_url = data['link']
    else:
        shorten_url = "Incorrect url"
    return shorten_url


def get_url_clicks(shorten_url):
    """
    Ф-ия принимает битлинк
    Ф-ия возвращает суммарное кол-во кликов
    """
    params = {
        'units': -1,
        'unit': 'day'
    }
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(shorten_url)
    response = requests.get(url, headers=headers, params=params)
    if response.ok:
        data = response.json()
        total_clicks = data['total_clicks']
    else:
        total_clicks = "Incorrect url"
    return total_clicks


def is_bitlink(url):
    """
    Ф-ия принимает url
    Ф-ия возвращает true/false, если url битлинк/не битлинк
    """
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url)
    response = requests.get(url, headers=headers)
    if response.ok:
        return True
    else:
        return False


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TOKEN")
    while True:
        input_url = input('Enter url:')
        if '//' in input_url:
            break
        else:
            print('Error: Enter correct URL (with http/s)')
    url_domain = input_url.split('//')[1]
    if is_bitlink(url_domain):
        total_clicks = get_url_clicks(url_domain)
        print(total_clicks)
    else:
        shorten_url = get_shorten_url(token, input_url)
        print(shorten_url)
