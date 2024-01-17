from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.sender.username

    def load_previous_messages(self, messages=10):
        return Message.objects.order_by('-timestamp').all()[:messages]