import requests
import os
from trace_dkey import trace

# OpenWeatherMap API example
def openweathermap_api_example():
    # You need to sign up for a free API key at https://openweathermap.org/
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY', 'your_api_key_here')
    city = "London"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # Find the path to the 'temp' key (current temperature)
    paths = trace(data, 'temp')
    print("Paths to 'temp':")
    for path in paths:
        print(" -> ".join(path))
        print(f"Value: {data['main']['temp']} K")

    # Find the path to the 'description' key (weather description)
    paths = trace(data, 'description')
    print("\nPaths to 'description':")
    for path in paths:
        print(" -> ".join(path))
        print(f"Value: {data['weather'][0]['description']}")

if __name__ == "__main__":
    openweathermap_api_example()