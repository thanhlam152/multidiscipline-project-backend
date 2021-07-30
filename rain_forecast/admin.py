from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.user import User
from .models.notification import Notification
from .models.device import Device
from .models.sensor import Sensor
from .models.magneticSwitch import MagneticSwitch
from .models.record import Record
from .models.door import Door


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'password')


admin.site.register(User, UserAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_read', 'time', 'to_user')


admin.site.register(Notification, NotificationAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic_name', 'aio_key', 'type')


admin.site.register(Device, DeviceAdmin)


class SensorAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'type')


admin.site.register(Sensor, SensorAdmin)


class MagneticSwitchAdmin(admin.ModelAdmin):
    list_display = ('get_name',)


admin.site.register(MagneticSwitch, MagneticSwitchAdmin)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'sensor', 'time', 'data')


admin.site.register(Record, RecordAdmin)


class DoorAdmin(admin.ModelAdmin):
    list_display = ('name', 'switch', 'type', 'status')


admin.site.register(Door, DoorAdmin)
