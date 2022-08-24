from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    kanban_group = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "address",
            "password",
            "email_id",
            "mobile_number",
            "kanban_group"
        ]
