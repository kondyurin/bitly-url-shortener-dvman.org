import requests


def get_weather_data(locations):
    weather_data = []
    payload = {'lang': 'ru', 'nTqm':''}
    url_template = 'http://wttr.in/{}'
    for location in locations:
        url = url_template.format(location)
        response = requests.get(url, params=payload)
        weather_data.append(response.text)
    return weather_data


if __name__ == "__main__":
    locations = ['лондон', 'svo', 'череповец']
    weather_data = get_weather_data(locations)
    for weather_location in weather_data:
        print(weather_location)