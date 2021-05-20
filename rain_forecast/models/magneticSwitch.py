from django.db import models
from django.db.models.deletion import CASCADE
from .device import Device


class MagneticSwitch(models.Model):

    id = models.OneToOneField(Device, primary_key=True, on_delete=CASCADE)    

    def __str__(self):
        return str(self.id)

    def get_name(self):
        return str(self.id)
