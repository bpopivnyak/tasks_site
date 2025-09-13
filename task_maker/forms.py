from django import forms
from .models import Task, Project



class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["title", "description", "status", "due_datetime", "project"]



