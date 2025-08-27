from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskDeleteView, TaskEditView

urlpatterns = [
    path('', TaskListView.as_view, name='task_list'),
    path('', TaskDetailView.as_view, name='task_detail'),
    path('', TaskCreateView.as_view, name='task_create'),
    path('', TaskDeleteView.as_view, name='task_delete'),
    path('', TaskEditView.as_view, name='task_edit')
]