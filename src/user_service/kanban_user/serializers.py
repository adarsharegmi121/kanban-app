from rest_framework import serializers
from kanban_user.models import KanbanUser


class KanbanUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanUser
        fields = ["group_name", "date_created"]
        extra_kwargs = {"boards": {"required": False}}
