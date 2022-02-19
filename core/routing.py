from channels.auth import AuthMiddlewareStack
# to add auth in the chat app or getting the user 
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        # wrapp it in AuthMiddlewareStack to add authentication
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
