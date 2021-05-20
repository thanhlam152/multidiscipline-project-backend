from rest_framework import serializers
from .models.user import User
from .models.notification import Notification
from .models.device import Device
from .models.sensor import Sensor
from .models.magneticSwitch import MagneticSwitch
from .models.record import Record
from .models.door import Door


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class MagneticSwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagneticSwitch
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = '__all__'
