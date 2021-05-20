from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rain_forecast import views as forecast_views


router = routers.DefaultRouter()
router.register(r'users', forecast_views.UserView)
router.register(r'notifications', forecast_views.NotificationView)
router.register(r'device', forecast_views.DeviceView)
router.register(r'sensor', forecast_views.SensorView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]