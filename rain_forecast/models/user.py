from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    password = models.TextField()

    def __str__(self):
        return self.name
        