from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from . import models
from .forms import TaskForm, CommentsForm
from .mixins import UserIsOwnerMixin
from .models import Task, Information

class MainInformationView(ListView):
    model = Information
    template_name = "Tasks/task_information_main.html"
    context_object_name = 'tasks'

class DetailInformationView(ListView):
    model = Information
    template_name = "Tasks/task_information.html"
    context_object_name = 'tasks'

class TaskListView(ListView):
    model = Task
    template_name = "Tasks/task-list.html"
    context_object_name = 'tasks'
    ordering = ['-published_at']

class TaskDetailView(DetailView):
    model = Task
    template_name = "Tasks/task_detail.html"
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comment_form'] = CommentsForm()
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentsForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.task = self.get_object()
            comment.save()
            return redirect('task_detail', pk=comment.task.pk)
        else:
            pass

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
    template_name = "Tasks/task_delete.html"
    success_url = reverse_lazy('task_list')
    context_object_name = 'task'


class TaskEditView(UpdateView):
    model = Task
    template_name = "Tasks/task_edit.html"
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    context_object_name = 'task'

class TaskCompleteView(LoginRequiredMixin, UserIsOwnerMixin, View):
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = "done"
        task.save()
        return HttpResponseRedirect (reverse_lazy("task_list"))

    def object(self):
        task_id = self.kwargs.get("pk")
        return get_object_or_404(models.Task, pk=task_id)

class CustomLoginView(LoginView):
    template_name = "Tasks/login.html"
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = "login"

class RegisterView(CreateView):
    template_name = "Tasks/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())
