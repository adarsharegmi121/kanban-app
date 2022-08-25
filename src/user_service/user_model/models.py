from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=30)
    email_id = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=12)

def __str__(self):
    return "%s %s %s " % (self.email_id)