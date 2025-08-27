from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import TaskForm
from .models import Tasks

class TaskListView(ListView):
    model = Tasks
    template_name =
    context_object_name =
    ordering = ['-published_at']

class TaskDetailView(DetailView):
    model = Tasks
    template_name =
    context_object_name =

class TaskCreateView(CreateView):
    model = Tasks
    template_name =
    form_class = TaskForm
    success_url = reverse_lazy('news_list')

class TaskDeleteView(DeleteView):
    model = Tasks
    template_name =
    success_url = reverse_lazy('news_list')

class TaskEditView(UpdateView):
    model = Tasks
    template_name =
    form_class = TaskForm
    success_url = reverse_lazy('news_list')