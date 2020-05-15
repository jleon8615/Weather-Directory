import requests

# API address information
API_root = 'https://www.metaweather.com'
API_location = '/api/location/search/?query='
API_weather = '/api/location/'

# Querry the location
def fetch_location(query):
    return requests.get(API_root + API_location + query).json()

# Querry the weather information
def fetch_weather(woeid):
    return requests.get(API_root + API_weather + str(woeid)).json()

# Displayed weather information
def display_weather(weather):
    print(f"Weather for {weather['title']}:")
    for entry in weather['consolidated_weather']:
        date = entry['applicable_date']
        high = entry['max_temp']
        low = entry['min_temp']
        state = entry['weather_state_name']
        print(f"{date}\t{state}\thigh {high:2.1f}°C\tlow {low:2.1f}°C")

# Suggestive locations base on ambiguity
def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['title']}")

# Verified user location input & test server and network
# exception errors
def weather_dialog():
    try:
        where = ''
        while not where:
            where = input("where in the wolrd are you?")
        locations = fetch_location(where)
        if len(locations) == 0:
            print("I don't know where that is.")
        elif len(locations) > 1:
            disambiguate_locations(locations)
        else:
            woeid = locations[0]['woeid']
            display_weather(fetch_weather(woeid))
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to the server. Is your network up?")




if __name__ == '__main__':
    while True:
        weather_dialog()