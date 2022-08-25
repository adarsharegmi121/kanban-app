from rest_framework import serializers
from user_model.models import User
from kanban_user.serializers import KanbanUserSerializer


class UserSerializer(serializers.ModelSerializer):
    kanban_group = KanbanUserSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "address",
            "password",
            "email_id",
            "mobile_number",
            "kanban_group",
        ]
