from rest_framework import serializers

from common import determine_background_color
from tasks_app.models import Location, Task
from weather_app.utils import get_weather_data


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model."""

    location_details = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {"location": {"write_only": True}}

    def get_location_details(self, obj: Task) -> dict:
        weather_data = get_weather_data(obj.location.name)

        return {
            "location_id": obj.location.id,
            "location_name": obj.location.name,
            "temperature": weather_data["main"]["temp"],
            "background_color": determine_background_color(weather_data),
        }

    def validate(self, data: dict) -> dict:
        """
        Check location constraints on the Task.
        """
        # Ensure that a location is specified for non-completed tasks
        if not data.get("completed") and not data.get("location"):
            raise serializers.ValidationError(
                "Location must be specified for active tasks."
            )
        return data


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
