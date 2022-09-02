import requests
from config import WEATHER_API_KEY, WEATHER_URL

def weather_by_city(city_name):
    weather_url = WEATHER_URL
    params = {
        'key': WEATHER_API_KEY,
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru'
    }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if 'location' in weather:
        if 'current' in weather:
            try:
                return weather['current']
            except (KeyError, TypeError):
                return False
    return False

if __name__ == '__main__':
    print(weather_by_city('Moscow'))