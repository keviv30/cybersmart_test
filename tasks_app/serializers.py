from rest_framework import serializers

from tasks_app.models import Location, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name"]
