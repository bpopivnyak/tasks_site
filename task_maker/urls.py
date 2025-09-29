from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskCompleteView, TaskDeleteView, TaskEditView, CustomLoginView, CustomLogoutView, RegisterView, MainInformationView, DetailInformationView

urlpatterns = [
    path('', MainInformationView.as_view(), name='information_page'),
    path('<int:pk>/', DetailInformationView.as_view(), name='information'),
    path('task-list/', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/detail/', TaskDetailView.as_view(), name='task_detail'),
    path('task-create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/complete/', TaskCompleteView.as_view(), name='task_complete'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/edit/', TaskEditView.as_view(), name='task_edit'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]