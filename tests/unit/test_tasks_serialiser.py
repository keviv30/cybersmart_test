from typing import Callable
from unittest.mock import patch

import pytest

from tasks_app.models import Location, Task
from tasks_app.serializers import LocationSerializer, TaskSerializer


@pytest.mark.django_db
def test_task_serializer_fields(
    create_task: Callable[[], Task], sample_location: Location
):
    with patch("tasks_app.serializers.get_weather_data") as mock_get_weather:
        # Setup mock return value
        mock_get_weather.return_value = {
            "weather": [{"main": "Clear"}],
            "main": {"temp": 15},
        }

        # Given
        task = create_task(
            title="Test Task 1",
            description="Test Task 1",
            completed=False,
            location=sample_location,
        )

        # When
        serializer = TaskSerializer(instance=task)

        # Then
        assert "id" in serializer.data
        assert "description" in serializer.data
        assert "completed" in serializer.data
        assert "location" in serializer.data
        assert "background_color" in serializer.data["weather_data"]
        assert "temperature" in serializer.data["weather_data"]


@pytest.mark.django_db
def test_task_serializer():
    # Given
    task_data = {
        "title": "Test Task",
        "description": "Test Task",
        "completed": False,
    }

    # When
    serializer = TaskSerializer(data=task_data)
    assert serializer.is_valid()
    serializer.save()

    # Then
    # Check the task was created
    assert Task.objects.count() == 1
    task_obj = Task.objects.get()
    assert task_obj.description == "Test Task"
    assert task_obj.completed is False


@pytest.mark.django_db
def test_location_serializer():
    # Given
    location = Location.objects.create(name="Test Location")

    # When
    serializer = LocationSerializer(location)
    data = serializer.data

    # Then
    # Check that the serialized data matches what's expected
    assert data["name"] == "Test Location"

    # Test deserialization (creating an instance from data)
    new_data = {"name": "New Test Location"}
    new_serializer = LocationSerializer(data=new_data)
    assert new_serializer.is_valid()
    new_location = new_serializer.save()

    # Verify the created instance
    assert new_location.name == "New Test Location"
