import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

from tasks_app.models import Location
from tasks_app.views import ListLocationView


@pytest.mark.django_db
def test_location_list(
    factory: APIRequestFactory, sample_location: Location
) -> None:
    url = reverse("locations-list")
    view = ListLocationView.as_view()

    request = factory.get(url)
    response = view(request, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == sample_location.name
