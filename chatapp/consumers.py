import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        messages = Message.load_previous_messages(10)
        content = {
            'messages': self.parse_to_json(messages)
        }
        self.send_chat_message(content)

    def new_message(self, data):
        sender = data['from']
        sender_user = User.objects.filter(username=sender)[0]
        message = Message.objects.create(sender=sender_user, content=data['message'])
        content = {
            'command': 'new_message',
            'message': self.parse_single_to_json(message)
        }
        return self.send_chat_message(content)

    def parse_to_json(self, messages):
        parsed = []
        for message in messages:
            parsed.append(self.parse_single_to_json(message))
        return parsed

    def parse_single_to_json(self, message):
        return {
            'sender': message.sender.username,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }
    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, 
            self.channel_name
            )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, 
            self.channel_name
            )
            
    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.commands[text_data_json['command']](self, text_data_json)
    
    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                "type": "chat.message", 
            "message": message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))