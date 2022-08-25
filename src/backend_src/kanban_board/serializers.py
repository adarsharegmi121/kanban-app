from rest_framework import serializers
from kanban_board.models import KanbanBoard
from kanban_user.serializers import KanbanUserSerializer


class KanbanBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanBoard
        fields = ["id","name", "description", "nickname", "kanban_group", "date_created"]
        extra_kwargs = {"date_created": {"required": False}}