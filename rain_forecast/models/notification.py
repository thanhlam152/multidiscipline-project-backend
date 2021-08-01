from django.db import models
from .user import User


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default='No title')
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
