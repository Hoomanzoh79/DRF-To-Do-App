from django.views import generic
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "tasks"
