import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch


@pytest.mark.django_db
def test_weather_data_view_success() -> None:
    # Mock the get_weather_data function
    with patch("weather_app.views.get_weather_data") as mock_get_weather:
        # Setup mock return value
        mock_get_weather.return_value = {
            "weather": [{"main": "Clear"}],
            "main": {"temp": 15},
        }

        client = APIClient()
        response = client.get(
            reverse("weather-data", kwargs={"location_name": "London"})
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["background_color"] == "red"
        assert response.data["temperature"] == 15
