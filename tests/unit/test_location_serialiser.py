import pytest

from tasks_app.models import Location
from tasks_app.serializers import LocationSerializer


@pytest.mark.django_db
def test_location_serializer_serialization(
    sample_location: Location, location_data: dict
) -> None:
    serializer = LocationSerializer(instance=sample_location)
    assert serializer.data["name"] == location_data["name"]
