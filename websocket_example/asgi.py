import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat import routing  # Make sure this imports your routing from chat

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_example.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns  # Use the websocket URL patterns
        )
    ),
})
