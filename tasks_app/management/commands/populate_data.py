from typing import List

from django.core.management.base import BaseCommand

from tasks_app.models import Location, Task


class Command(BaseCommand):
    help = "Add sample data to the database"

    def handle(self, *args, **kwargs):
        print("Clearing database")

        Task.objects.all().delete()
        Location.objects.all().delete()

        # Add sample data
        print("Adding sample locations")

        locations: List[Location] = list()
        for location in ["London", "Paris", "Berlin", "Tokyo", "Singapore"]:
            locations.append(Location(name=location))

        Location.objects.bulk_create(locations)
