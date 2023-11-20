from django.urls import path
from tasks_app.views import ListCreateTasksView, RetrieveUpdateDestroyTasksView


urlpatterns = [
    path("tasks/", ListCreateTasksView.as_view(), name="tasks-list-create"),
    path("tasks/<int:pk>/", RetrieveUpdateDestroyTasksView.as_view(), name="tasks-retrieve-update-destroy"),
]
