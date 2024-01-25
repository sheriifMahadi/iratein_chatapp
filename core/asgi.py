import os
from django.conf.urls import url

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")


from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()

from chatapp.middleware import TokenAuthMiddleware 
import chatapp.routing


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": TokenAuthMiddleware(URLRouter(chatapp.routing.websocket_urlpatterns))
    }
)

# "websocket": AllowedHostsOriginValidator(
#             AuthMiddlewareStack(URLRouter(websocket_urlpatterns)))