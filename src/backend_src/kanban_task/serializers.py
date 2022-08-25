from rest_framework import serializers
from kanban_lane.models import KanbanTask

class KanbaTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanTask
        fields = ["title", "description", "status", "lane"]