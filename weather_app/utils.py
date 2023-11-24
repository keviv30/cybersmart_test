# utils.py
import os

import requests
from django.conf import settings

from .exceptions import WeatherDataFetchError


def get_weather_data(location_name: str) -> dict:
    api_key = str(os.getenv("WEATHER_API_KEY"))
    try:
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={location_name}&units=metric&appid={api_key}"
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise WeatherDataFetchError(f"Error fetching weather data: {e}")
