from rest_framework import generics

from tasks_app.models import Location, Task
from tasks_app.serializers import LocationSerializer, TaskSerializer


class ListCreateTasksView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RetrieveUpdateDestroyTasksView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ListLocationView(generics.ListAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
