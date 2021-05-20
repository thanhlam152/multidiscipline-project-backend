from django.db import models
from django.db.models.deletion import CASCADE
from .device import Device


class Sensor(models.Model):

    SENSOR_TYPE = [
      ('RS', 'rain sensor'),
      ('TS', 'temperature sensor'),
      ('WS','wind sensor')
    ]

    id = models.OneToOneField(Device, primary_key=True, on_delete=CASCADE)
    type = models.CharField(max_length=2, choices=SENSOR_TYPE, default='RS')
    

    def __str__(self):
        return str(self.id)

    def get_name(self):
        return str(self.id)
