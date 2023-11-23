import pytest

from tasks_app.models import Location, Task


@pytest.mark.django_db
def test_create_task():
    # Setup test data
    location = Location.objects.create(name="Home")

    # Create a Task instance
    task = Task.objects.create(
        title="Test Task",
        description="Test Task",
        completed=False,
        location=location,
    )

    # Assertions
    assert task.description == "Test Task"
    assert task.completed is False
    assert task.location == location
