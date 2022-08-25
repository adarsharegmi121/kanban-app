from django.contrib import admin
from django.urls import path
from kanban_task.views import KanbanTaskAPIView, KanbanTaskDetailView

urlpatterns = [
    path("api/task/", KanbanTaskAPIView.as_view()),
    path("api/task/<str:task_id>/", KanbanTaskDetailView.as_view()),
]
