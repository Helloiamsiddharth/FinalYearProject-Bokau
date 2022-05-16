from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from vechile.middleware import TokenAuthMiddlewareStack
from trips.consumers import TaxiConsumer

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': TokenAuthMiddlewareStack( # changed
        URLRouter([
            path('vechile/', TaxiConsumer.as_asgi()),
        ])
    ),
})