from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task-create/', TaskCreateView.as_view(), name='task_create'),
#    path('', TaskDeleteView.as_view, name='task_delete'),
#    path('', TaskEditView.as_view, name='task_edit')
]