from typing import List

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from tasks_app.models import Task, Location


class Command(BaseCommand):
    help = "Add sample data to the database"

    def handle(self, *args, **kwargs):
        print("Clearing database")

        User.objects.all().delete()
        Task.objects.all().delete()
        Location.objects.all().delete()

        # Add sample data
        print("Adding sample user and locations")
        User.objects.create_user(username="Testuser", password="testpass123")

        locations: List[Location] = list()
        for location in ["London", "Paris", "Berlin", "Tokyo", "Singapore"]:
            locations.append(Location(name=location))

        Location.objects.bulk_create(locations)
