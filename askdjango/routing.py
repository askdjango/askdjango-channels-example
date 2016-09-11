from channels.routing import include, route

channel_routing = [
    # route('http.request', 'chat.consumers.http_consumer'),
    include('blog.routing.channel_routing', path='^/blog/'),
    include('chat.routing.channel_routing', path='^/chat/'),
]

