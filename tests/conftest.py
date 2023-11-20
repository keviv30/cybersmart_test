import pytest
from django.contrib.auth.models import User

from tasks_app.models import Task


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
