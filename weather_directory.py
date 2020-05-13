import requests

API_root = 'https://www.metaweather.com'
API_location = '/api/location/search/?query='
API_weather = '/api/location/'

def fetch_location(query):
    return requests.get(API_root + API_location + query).json()


def fetch_weather(woeid):
    return requests.get(API_root + API_weather + str(woeid)).json()


