from django import forms
from .models import Task, Comment



class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["title", "description", "status", "due_datetime", "project"]

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["media", "content"]
        widgets = {
            "media": forms.FileInput()
        }

