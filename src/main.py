import json

from utils.api_integration import get_route_data, get_weather_data


def main():
    # Coordinates: San Francisco to Los Angeles (example)
    origin_coords = (-122.4194, 37.7749)  # San Francisco (long,lat)
    destination_coords = (-118.2437, 340522)  # Los Angeles (long, lat)

    print("Fetching route data...")
    route_data = get_route_data(origin_coords, destination_coords)
    if route_data:
        print("route data retrieved successfully")
        print(json.dump(route_data, indent=4))  # Pretty print the route data

    print("\nFetching weather data...")
    location = (37.7749, -122.4194)  # SF (lat, long)
    weather_data = get_weather_data(location)
    if weather_data:
        print("Weather data retrieved successfully")
        print(json.dumps(weather_data, indent=4)) # Pretty print the weather data

if __name__ == "__main__":
    pass
