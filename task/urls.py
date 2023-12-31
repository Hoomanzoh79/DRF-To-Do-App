from django.urls import path, include
from . import views

app_name = "task"

urlpatterns = [
    path("list/", views.TaskListView.as_view(), name="list"),
    # Api
    path("api/v1/", include("task.api.v1.urls")),
]
