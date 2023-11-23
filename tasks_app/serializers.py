from rest_framework import serializers

from tasks_app.models import Location, Task
from common import determine_background_color
from weather_app.utils import get_weather_data


class TaskSerializer(serializers.ModelSerializer):
    weather_data = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"

    def validate(self, data):
        """
        Check location constraints on the Task.
        """
        # Ensure that a location is specified for non-completed tasks
        if not data.get("completed") and not data.get("location"):
            raise serializers.ValidationError(
                "Location must be specified for active tasks."
            )
        return data

    def get_weather_data(self, obj):
        weather_data = get_weather_data(obj.location.name)

        return {
            "background_color": determine_background_color(weather_data),
            "temperature": weather_data["main"]["temp"],
        }


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
