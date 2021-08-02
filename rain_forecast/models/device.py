from django.db import models
from django.db.models.deletion import CASCADE
from .user import User


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic_name = models.CharField(max_length=255, unique=True, null=True)
    aio_key = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.topic_name
