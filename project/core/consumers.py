from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from . models import *

class MyWebsocketConsumer(WebsocketConsumer):
  def connect(self):
    print("Websocket connected...")
    print("Channel Layer...",self.channel_layer)
    print("Channel Name...",self.channel_name)
    self.group_name = self.scope['url_route']['kwargs']['group_nm']
    # self.group_name 
    async_to_sync(self.channel_layer.group_add)(
      self.group_name,
      self.channel_name
    )
    self.accept()

  def receive(self, text_data=None, bytes_data=None):
    print('Message Received From The Client...',text_data)
    print(type(text_data))
    data = json.loads(text_data)
    print(data['msg'])
    message = data['msg']
    async_to_sync(self.channel_layer.group_send)(
      self.group_name,
      {
        'type':'chat.message',
        'message':message
      }
    )
    # message = data['']
  def chat_message(self, event):
    self.send(text_data = json.dumps({
      'msg':event['message']
    }))