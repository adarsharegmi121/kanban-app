from rest_framework import serializers
from kanban_task.models import KanbanTask

class KanbanTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanTask
        fields = ["id","title", "description", "status", "lane"]