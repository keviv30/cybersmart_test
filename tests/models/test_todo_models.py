import pytest
from django.contrib.auth.models import User
from todo_app.models import Task


@pytest.mark.django_db
def test_create_task():
    # Setup test data
    user = User.objects.create_user(username="testuser", password="12345")
    location = Location.objects.create(name="Home")

    # Create a Task instance
    task = Task.objects.create(
        owner=user,
        title="Test Task",
        description="Test Task",
        completed=False,
        location=location
    )

    # Assertions
    assert task.owner == user
    assert task.description == "Test Task"
    assert task.completed is False
    assert task.location == location
