# test_weather.py
import pytest

from common import determine_background_color


@pytest.mark.parametrize(
    "weather_data, expected_color",
    [
        ({"weather": [{"main": "Snow"}]}, "blue"),
        ({"weather": [{"main": "Rain"}]}, "blue"),
        ({"weather": [{"main": "Clear"}]}, "red"),
        ({"weather": [{"main": "Clouds"}]}, "orange"),
        (
            {"weather": [{"main": "Mist"}]},
            "gray",
        ),  # Testing an undefined weather condition
    ],
)
def test_determine_background_color(
    weather_data: dict, expected_color: str
) -> None:
    assert determine_background_color(weather_data) == expected_color
