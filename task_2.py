import requests


def get_shorten_url(token, url):
    payload = {
        'long_url': url
    }
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    return data['link']


if __name__ == "__main__":
    token = 'e412cdcb5d63a89ba3626f64e77352258aa42bd9'
    long_url = input('Enter url:')
    shorten_url = get_shorten_url(token, long_url)
    print(shorten_url)