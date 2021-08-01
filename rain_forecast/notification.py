from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
from requests.exceptions import ConnectionError, HTTPError


# Basic arguments. You should extend this function with the push features you
# want to use, or simply pass in a `PushMessage` object.
def send_push_message(token, title, message, extra=None):
    response = PushClient().publish(
        PushMessage(
            sound='default',
            title=title,
            body=message,
            to=token))


send_push_message('ExponentPushToken[dmN4gyNzeBkJZrbrMLmXSe]', 'test', 'test')
