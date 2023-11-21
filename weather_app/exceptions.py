# exceptions.py


class WeatherDataFetchError(Exception):
    """Exception raised when fetching weather data fails."""

    def __init__(self, message="Failed to fetch weather data"):
        self.message = message
        super().__init__(self.message)
