from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import TaskForm
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = "Tasks/task_list.html"
    context_object_name = 'tasks'
    ordering = ['-published_at']

class TaskDetailView(DetailView):
    model = Task
    template_name = "Tasks/task_detail.html"
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    template_name = "Tasks/task_form"
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

#class TaskDeleteView(DeleteView):
#    model = Task
#    template_name =
#    success_url = reverse_lazy('task_list')

#class TaskEditView(UpdateView):
#    model = Task
#   template_name =
#    form_class = TaskForm
#    success_url = reverse_lazy('task_list')