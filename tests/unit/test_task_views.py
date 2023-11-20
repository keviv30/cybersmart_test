from typing import Callable

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from tasks_app.models import Location, Task
from tasks_app.views import ListCreateTasksView, RetrieveUpdateDestroyTasksView


@pytest.mark.django_db
def test_create_task(test_user: User, factory: APIRequestFactory) -> None:
    # Given
    location = Location.objects.create(name="London")
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

    view = ListCreateTasksView.as_view()

    # When
    request = factory.post(url, data)
    response = view(request)

    # Then
    assert response.status_code == 201
    assert response.data["description"] == data["description"]


@pytest.mark.django_db
def test_retrieve_tasks(
    test_user: User,
    create_task: Callable[[], Task],
    factory: APIRequestFactory,
) -> None:
    # Given
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

    url = reverse(
        "tasks-list-create"
    )  # Update with the correct URL name for task listing

    view = ListCreateTasksView.as_view()

    # When
    request = factory.get(url, format="json")
    response = view(request)

    # Then
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_update_task(
    factory: APIRequestFactory,
    test_user: User,
    create_task: Callable[[], Task],
    sample_location: Location,
) -> None:
    # Given
    test_task = create_task(
        owner=test_user,
        title="Test Task 1",
        description="Test Task 1",
        completed=False,
        location=sample_location,
    )

    updated_task = {"description": "Updated Task", "completed": True}
    url = reverse(
        "tasks-retrieve-update-destroy",
        kwargs={"pk": test_task.id},
    )

    view = RetrieveUpdateDestroyTasksView.as_view()

    # When
    request = factory.patch(url, updated_task)
    response = view(request, pk=test_task.id)

    # Then
    assert response.status_code == 200
    updated_task = Task.objects.get(id=test_task.id)
    assert updated_task.description == "Updated Task"
    assert updated_task.completed is True


@pytest.mark.django_db
def test_delete_task(
    factory: APIRequestFactory, test_user, create_task, sample_location
):
    # Given
    test_task = create_task(
        owner=test_user,
        title="Test Task 1",
        description="Test Task 1",
        completed=False,
        location=sample_location,
    )

    url = reverse(
        "tasks-retrieve-update-destroy",
        kwargs={"pk": test_task.id},
    )

    view = RetrieveUpdateDestroyTasksView.as_view()

    # When
    request = factory.delete(url)
    response = view(request, pk=test_task.id)

    # Then
    assert response.status_code == 204
    with pytest.raises(Task.DoesNotExist):
        Task.objects.get(id=test_task.id)
