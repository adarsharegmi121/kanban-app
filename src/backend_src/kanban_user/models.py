from django.db import models
from user_model.models import User

# Create your models here.
class KanbanUser(models.Model):
    group_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    # for kanban group and users relationship (M2M)
    users = models.ManyToManyField(User, blank=True, related_name="users")

    class Meta:
        ordering = ["date_created", "group_name"]
