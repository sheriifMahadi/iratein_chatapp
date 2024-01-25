from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from chatapp_api.views import UserViewSet, ConversationViewSet, MessageViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("conversations", ConversationViewSet)
router.register("users", UserViewSet)
router.register("messages", MessageViewSet)


# app_name = "api"
urlpatterns = router.urls