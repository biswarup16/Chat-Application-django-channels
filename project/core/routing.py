from django.urls import path
from . consumers import *

websocket_urlpatterns = [
  path('ws/sc/<str:group_nm>/', MyWebsocketConsumer.as_asgi()),
  # path('ws/ac/<str:groupkaname>/', consumers.MyAsyncConsumer.as_asgi()),
]