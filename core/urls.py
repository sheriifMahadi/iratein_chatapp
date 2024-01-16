from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chatapp.urls', namespace='chatapp')),
    path('api/', include('chatapp_api.urls', namespace='chatapp_api'))
]
