from django.db import models
from django.db.models.deletion import CASCADE
from .user import User

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    register_user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name
