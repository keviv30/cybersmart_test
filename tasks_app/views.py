from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from tasks_app.models import Task
from tasks_app.serializers import TaskSerializer


class ListCreateTasksView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RetrieveUpdateDestroyTasksView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
