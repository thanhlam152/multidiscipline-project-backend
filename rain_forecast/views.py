from django.contrib.auth.hashers import check_password
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import Serializer

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

    def list(self, request):
        userId = self.request.query_params.get('user')

        notificationList = Notification.objects.all()
        if userId:
            user = get_object_or_404(User, id=userId)
            notificationList = notificationList.filter(to_user=user)

        serializer = NotificationSerializer(notificationList, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


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


class LoginView(viewsets.ViewSet):
    def create(self, request):
        print(request.data)
        user = get_object_or_404(User, email=request.data.get("email"))
        if check_password(request.data.get("password"), user.password):
            serializer = UserSerializer(user)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "message": "Not found"
            },
            status=status.status.HTTP_404_NOT_FOUND
        )
