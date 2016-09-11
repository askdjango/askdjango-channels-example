from channels.routing import route
from . import consumers

channel_routing = [
    route('websocket.connect', consumers.ws_add),
    route('websocket.receive', consumers.ws_message),
    route('websocket.disconnect', consumers.ws_disconnect),
]

