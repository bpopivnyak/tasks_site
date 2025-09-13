from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from .forms import TaskForm
from .mixins import UserIsOwnerMixin
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = "Tasks/task_list.html"
    context_object_name = 'tasks'
    ordering = ['-published_at']

class TaskDetailView(DetailView):
    model = Task
    template_name = "Tasks/task_detail.html"
    context_object_name = 'tasks'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "Tasks/task_form"
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "Task/task_delete"
    success_url = reverse_lazy('task_list')

class TaskEditView(UpdateView):
    model = Task
    template_name = "Tasks/task_edit"
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

class TaskCompleteView(LoginRequiredMixin, UserIsOwnerMixin, View):
    def post(self, request):
        task = self.get_object()
        task.status = "done"
        task.save()
        return HttpResponseRedirect (reverse_lazy("tasks:task_list"))

    def object(self):
        task_id = self.kwargs.get("pk")
        return get_object_or_404(models.Task, pk=task_id)