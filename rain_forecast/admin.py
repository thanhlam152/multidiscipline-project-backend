from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.user import User
from .models.notification import Notification


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'password')


admin.site.register(User, UserAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'is_read', 'time', 'to_user')


admin.site.register(Notification, NotificationAdmin)
