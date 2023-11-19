from django.urls import path
from tasks_app.views import ListCreateTasksView


urlpatterns = [
    path("tasks/", ListCreateTasksView.as_view(), name="tasks-list-create"),
]
