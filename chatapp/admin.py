from django.contrib import admin
from .models import Message


# Register your models here.
 
from django.contrib import admin
from .models import Conversation, Message
 
 
admin.site.register(Conversation)
admin.site.register(Message)