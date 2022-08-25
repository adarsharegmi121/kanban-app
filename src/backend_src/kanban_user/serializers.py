from rest_framework import serializers
from kanban_user.models import KanbanUser
from user_model.models import User

class KanbanUserSerializer(serializers.ModelSerializer):
    users= serializers.SlugRelatedField(many=True, slug_field="email_id", queryset=User.objects.all())
    class Meta:
        model = KanbanUser
        fields = ["id", "group_name", "date_created", "users"]
        extra_kwargs = {"date_created": {"required": False}}
        depth=1
        