from django.urls import path
from . import views


urlpatterns = [
    path('tasks/',views.TaskList.as_view(),name='task-list'),
    # path('tasks/<int:pk>/',views.task_detail,name='task-detail'),
]
