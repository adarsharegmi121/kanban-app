from django.contrib import admin
from django.urls import path
from kanban_lane.views import KanbanLaneAPIView, KanbanLaneDetailView

urlpatterns = [
    path("api/lane/", KanbanLaneAPIView.as_view()),
    path("api/lane/<str:lane_id>/", KanbanLaneDetailView.as_view()),
]
