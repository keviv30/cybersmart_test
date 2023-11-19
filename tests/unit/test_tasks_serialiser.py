import pytest
from django.contrib.auth.models import User
from tasks_app.models import Task
from tasks_app.serializers import TaskSerializer


@pytest.mark.django_db
def test_task_serializer():
    # Create a test user
    test_user = User.objects.create_user(username="testuser", password="testpass123")

    # Data for creating a new task
    task_data = {
        "owner": test_user.id,
        "title": "Test Task",
        "description": "Test Task",
        "completed": False
    }

    # Use the serializer to create a new task
    serializer = TaskSerializer(data=task_data)
    assert serializer.is_valid()
    serializer.save()

    # Check the task was created
    assert Task.objects.count() == 1
    task_obj = Task.objects.get()
    assert task_obj.description == 'Test Task'
    assert task_obj.completed is False
    assert task_obj.owner == test_user
