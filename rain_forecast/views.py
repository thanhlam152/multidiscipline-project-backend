import re
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response

from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from .models.user import User
from .models.notification import Notification

from .serializers import UserSerializer, NotificationSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NotificationView(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
