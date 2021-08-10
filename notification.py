from backend import setup
setup()


from exponent_server_sdk import (
    PushClient,
    PushMessage,
)
from rain_forecast.models import User, Notification

# Basic arguments. You should extend this function with the push features you
# want to use, or simply pass in a `PushMessage` object.
def send_push_message(token, title, message, extra=None):
    response = PushClient().publish(
        PushMessage(
            sound='default',
            title=title,
            body=message,
            to=token))
    userList = list(User.objects.values_list('id', flat=True))
    currentUser = User.objects.get(id=userList[-1])
    newNotificaion = Notification(title=title,content=message,to_user=currentUser)
    newNotificaion.save()


# send_push_message('ExponentPushToken[psuQ8ZGEELL-Twb17-6-SD]', 'test', 'test')
