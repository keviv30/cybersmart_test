import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from tasks_app.models import Location, Task
from django.contrib.auth.models import User
from typing import Callable


@pytest.mark.django_db
def test_create_task(test_user: User) -> None:
    # Given
    location = Location.objects.create(name="London")
    client = APIClient()
    client.force_authenticate(user=test_user)
    url = reverse(
        "tasks-list-create"
    )  # Update with the correct URL name for task creation
    data = {
        "owner": test_user.id,
        "title": "Test Task",
        "description": "Test Task description",
        "completed": False,
        "location": location.id,
    }

    # When
    response = client.post(url, data, format="json")

    # Then
    assert response.status_code == 201
    assert response.data["description"] == data["description"]


@pytest.mark.django_db
def test_retrieve_tasks(
    test_user: User, create_task: Callable[[], Task]
) -> None:
    create_task(
        owner=test_user,
        title="Test Task 1",
        description="Test Task 1",
        completed=False,
    )
    create_task(
        owner=test_user,
        title="Test Task 2",
        description="Test Task 2",
        completed=False,
    )

    client = APIClient()
    client.force_authenticate(user=test_user)
    url = reverse(
        "tasks-list-create"
    )  # Update with the correct URL name for task listing
    response = client.get(url, format="json")

    assert response.status_code == 200
    assert len(response.data) == 2
