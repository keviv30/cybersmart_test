from rest_framework import serializers
from tasks_app.models import Task, Location


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "title",
            "description",
            "completed",
            "location",
        ]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name"]
