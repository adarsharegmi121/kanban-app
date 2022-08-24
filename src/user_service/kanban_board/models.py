from django.db import models
from kanban_user.models import KanbanUser

# Create your models here.
class KanbanBoard(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_created=True)
    description = models.CharField(max_length=1000)
    nickname = models.CharField(max_length=50)
    kanban_group = models.ForeignKey(KanbanUser ,on_delete=models.CASCADE, related_name="kanban_group")
