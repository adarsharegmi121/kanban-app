from django.db import models
from kanban_lane.models import KanbanLane

class KanbanTask(models.Model):
    STATUS_CHOICES = [
       ('PENDING', 'pending task'),
       ('DONE', 'Completed task'),
       ('NG', 'Not assigned'),
       ('IN work', 'working currently')
   ]
    title=models.CharField(max_length=21)
    description=models.CharField(max_length=99)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    lane = models.ForeignKey(KanbanLane, on_delete=models.CASCADE)