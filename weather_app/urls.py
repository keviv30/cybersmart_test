from django.urls import path
from weather_app.views import WeatherDataView

urlpatterns = [
    path('weather/<str:location_name>/', WeatherDataView.as_view(), name='weather-data'),
]