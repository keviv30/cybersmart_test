import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from tasks_app.models import Location
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_task():
    # Given
    user = User.objects.create_user(
        username="testuser", password="testpass123"
    )
    location = Location.objects.create(name="London")
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse(
        "tasks-list-create"
    )  # Update with the correct URL name for task creation
    data = {
        "owner": user.id,
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
