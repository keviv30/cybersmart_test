from typing import Callable

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tasks_app.models import Location, Task


@pytest.mark.django_db
def test_create_task(client: APIClient, sample_location: Location):
    location_url = reverse("locations-list")
    location_response = client.get(location_url)

    url = reverse("tasks-list-create")
    data = {
        "title": "Test Task",
        "description": "Test Task",
        "location": location_response.data[0]["id"],
        "completed": False,
    }

    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["description"] == "Test Task"


@pytest.mark.django_db
def test_retrieve_tasks(client: APIClient):
    url = reverse("tasks-list-create")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_task_success(
    client: APIClient,
    create_task: Callable[[], Task],
    sample_location: Location,
):
    test_task = create_task(
        title="Test Task",
        description="Test Task",
        completed=False,
        location=sample_location,
    )
    url = reverse("tasks-retrieve-update-destroy", kwargs={"pk": test_task.id})
    data = {"description": "Updated Task", "completed": True}
    response = client.patch(url, data, content_type="application/json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["description"] == "Updated Task"
    assert response.data["completed"] is True
