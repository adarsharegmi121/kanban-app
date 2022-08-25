from rest_framework import serializers
from kanban_lane.models import KanbanLane

class KanbanLaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanLane
        fields = ["id","lane_name", "date_created", "board"]
        extra_kwargs = {"date_created": {"required": False}}