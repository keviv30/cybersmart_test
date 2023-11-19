import logging
from tasks_app.serializers import TaskSerializer
from rest_framework import generics


class ListCreateTasksView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
