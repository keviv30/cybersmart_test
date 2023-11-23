import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tasks_app.models import Location


@pytest.mark.django_db
def test_create_task(client: APIClient, sample_location: Location):
    url = reverse("tasks-list-create")
    data = {
        "title": "Test Task",
        "description": "Test Task",
        "location": sample_location.id,
        "completed": False,
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["description"] == "Test Task"
