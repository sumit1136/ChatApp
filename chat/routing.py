from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'wss/chat/(?P<room_name>\ws+)/$', consumers.ChatConsumer.as_asgi()),
]