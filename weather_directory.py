import requests

API_root = 'https://www.metaweather.com'
API_location = '/api/location/search/?query='
API_weather = '/api/location/'

def fetch_location(query):
    return requests.get(API_root + API_location + query).json()


def fetch_weather(woeid):
    return requests.get(API_root + API_weather + str(woeid)).json()


def display_weather(weather):
    print(f"Weather for {weather['title']}:")
    for entry in weather['consolidated_weather']:
        date = entry['application_date']
        high = entry['max_temp']
        low = entry['min_temp']
        state = entry['weather_state_name']
        print(f"{date}\t{state}\thigh {high:2.1f}°C\tlow {low:2.1f}°C")
    

        
