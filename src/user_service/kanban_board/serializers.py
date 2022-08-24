from rest_framework import serializers
from kanban_board.models import KanbanBoard
from kanban_user.serializers import KanbanUserSerializer


class KanbanBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanBoard
        fields = ["name", "description", "nickname", "kanban_group"]