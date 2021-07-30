from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField
from .magneticSwitch import MagneticSwitch


class Door(models.Model):

    DOOR_TYPE = [
      ('DR', 'Main door'),
      ('WD', 'Window'),
    ]

    DOOR_STATUS = [
      ('CL', 'Closed'),
      ('OP', 'Open'),
    ]

    name = CharField(max_length=20, primary_key=True)
    switch = models.ForeignKey(MagneticSwitch, on_delete=CASCADE)
    type = models.CharField(max_length=2, choices=DOOR_TYPE, default='DR')
    status = models.CharField(max_length=2, choices=DOOR_STATUS, default='CL')

    def __str__(self):
        return self.name
