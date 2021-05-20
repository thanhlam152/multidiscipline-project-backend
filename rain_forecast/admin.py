from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.user import User
from .models.notification import Notification
from .models.device import Device
from .models.sensor import Sensor


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'password')


admin.site.register(User, UserAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'is_read', 'time', 'to_user')


admin.site.register(Notification, NotificationAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')


admin.site.register(Device, DeviceAdmin)


class SensorAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'type')


admin.site.register(Sensor, SensorAdmin)
