import pytest
from django.contrib.auth.models import User
from tasks_app.models import Task, Location
from tasks_app.serializers import TaskSerializer, LocationSerializer


@pytest.mark.django_db
def test_task_serializer():
    # Given
    test_user = User.objects.create_user(
        username="testuser", password="testpass123"
    )
    task_data = {
        "owner": test_user.id,
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
    assert task_obj.owner == test_user


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

