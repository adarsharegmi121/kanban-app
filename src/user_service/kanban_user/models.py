from tkinter import CASCADE
from django.db import models
from user_model.models import User

# Create your models here.
class KanbanUser(models.Model):
    group_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_created=True)
    users = models.ManyToManyField(User, blank=True, related_name="board")
    # for kanban group and users relationship (M2M)


    class Meta:
        ordering = ["date_created", "group_name"]
