# views.py

from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from common import determine_background_color
from .utils import get_weather_data
from .exceptions import WeatherDataFetchError


class WeatherDataView(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        location_name = kwargs.get("location_name", None)
        if location_name:
            try:
                weather_data = get_weather_data(location_name)
                return Response(
                    {
                        "background_color": determine_background_color(
                            weather_data
                        ),
                        "temperature": weather_data["main"]["temp"],
                    }
                )
            except WeatherDataFetchError as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        else:
            return Response(
                {"error": "Location name is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
