from django.db import models
from kanban_board.models import KanbanBoard
# Create your models here.

class KanbanLane(models.Model):
    lane_name= models.CharField(max_length=40)
    date_created=models.DateField(auto_now=True)
    board = models.ForeignKey(KanbanBoard, on_delete=models.CASCADE)