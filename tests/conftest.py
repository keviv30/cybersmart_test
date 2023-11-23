import pytest
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
def create_task():
    def _create_task(**kwargs):
        return Task.objects.create(**kwargs)

    return _create_task


@pytest.fixture
def location_data():
    return {"name": "London"}


@pytest.fixture
@pytest.mark.django_db
def sample_location(location_data: dict):
    return Location.objects.create(**location_data)
