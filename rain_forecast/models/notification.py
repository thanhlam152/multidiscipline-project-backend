from django.db import models
from .user import User

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    is_read = models.BooleanField()
    time = models.DateTimeField()
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
