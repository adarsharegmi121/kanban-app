from rest_framework import serializers
from kanban_user.models import KanbanUser
from user_model.serializers import UserSerializer

class KanbanUserSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = KanbanUser
        fields = ["id", "group_name", "date_created", "users"]
        extra_kwargs = {"date_created": {"required": False}}