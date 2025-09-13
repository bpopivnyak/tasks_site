from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskCompleteView, TaskDeleteView, TaskEditView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task-create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/complete/', TaskCompleteView.as_view(), name='task_complete'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/edit/', TaskEditView.as_view(), name='task_edit')
]