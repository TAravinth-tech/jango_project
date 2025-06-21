# chat/routing.py
from django.urls import re_path
from . import consumers

# WebSocket URL patterns
websocket_urlpatterns = [
    # WebSocket route for 'ws/chat/'
    

    # WebSocket route for 'ws/chat/general/' for a specific room
    # For dynamic room names
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
 # This is the route for /ws/chat/general/
]
