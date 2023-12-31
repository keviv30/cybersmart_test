from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title
