from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rain_forecast import views as forecast_views


router = routers.DefaultRouter()
router.register(r'users', forecast_views.UserView)
router.register(r'notifications', forecast_views.NotificationView)
router.register(r'devices', forecast_views.DeviceView)
router.register(r'sensors', forecast_views.SensorView)
router.register(r'magneticSwitchs', forecast_views.MagneticSwitchView)
router.register(r'records', forecast_views.RecordView)
router.register(r'doors', forecast_views.DoorView)
router.register(r'auth/login', forecast_views.LoginView, basename='login')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
