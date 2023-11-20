import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APIRequestFactory

from tasks_app.models import Location, Task


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def factory():
    return APIRequestFactory()


@pytest.fixture
@pytest.mark.django_db
def test_user():
    return User.objects.create_user(
        username="testuser", password="testpass123"
    )


@pytest.fixture
@pytest.mark.django_db
def create_task():
    def _create_task(**kwargs):
        return Task.objects.create(**kwargs)

    return _create_task


@pytest.fixture
@pytest.mark.django_db
def sample_location():
    return Location.objects.create(name="London")
