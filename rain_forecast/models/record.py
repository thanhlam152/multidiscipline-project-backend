from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey
from .sensor import Sensor


class Record(models.Model):

    id = AutoField(primary_key=True)
    sensor = ForeignKey(Sensor, on_delete=CASCADE)
    time = models.TimeField()
    data = models.FloatField()

    def __str__(self):
        return self.data
