from rest_framework import viewsets

from .models.user import User
from .models.notification import Notification
from .models.device import Device
from .models.sensor import Sensor
from .models.magneticSwitch import MagneticSwitch
from .models.record import Record
from .models.door import Door

from .serializers import *


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NotificationView(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class DeviceView(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class SensorView(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MagneticSwitchView(viewsets.ModelViewSet):
    queryset = MagneticSwitch.objects.all()
    serializer_class = MagneticSwitchSerializer


class RecordView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class DoorView(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer

