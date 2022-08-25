from django.contrib import admin
from django.urls import path
from kanban_user.views import KanbanUserAPIView, KanbanUserDetailView

urlpatterns = [
    path("api/kanban_user/", KanbanUserAPIView.as_view()),
    path("api/kanban_user/<str:group_id>/", KanbanUserDetailView.as_view()),
]
