from rest_framework import serializers
from kanban_task.models import KanbanTask

class KanbanTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanTask
        fields = ["title", "description", "status", "lane"]