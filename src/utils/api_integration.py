from http.client import responses

import openrouteservice
import requests
import json

# Load configuration
with open('config/config.json') as config_file:
    config = json.load(config_file)

ORS_API_KEY = config['openroutesservie_api_key']
WEATHER_API_KEY = config['weather_api_key']

# Initialize OpenRouteService client
ors_client = openrouteservice.Client(key=ORS_API_KEY)

def get_route_data(origin_coords, desitnation_coords):
    """
    Fetch route data from OpenRouteService.
    :param origin_coords: Tuple (latitude, longitude) of the starting location
    :param desitnation_coords: Tuple (latitude, longitude) of the destination
    :return:
    """

    try:
        route = ors_client.directions(
            coordinates = [origin_coords, desitnation_coords],
            profile = 'driving-car', # USe car-based routing
            format = 'geojson'
        )
        return route
    except openrouteservice.exceptions.ApiError as e:
        print(f'Error fetching route data: {e}')
        return None

def get_weather_data(location):
    """
    Fetch weather data for specific locaiton form OpenWeatherMap.
    :param location:  Tuple (latitudue, longitude) of the locaiton
    :return:  JSON resonse  with weather data
    """

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={location[0]}&lon={location[1]}&appid={WEATHER_API_KEY}"
        response = requests.get(url)
        response.raise_for_status() # Raise HTTPError for bad response
        return response.json()
    except  requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

