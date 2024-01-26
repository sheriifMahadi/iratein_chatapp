from django.contrib import admin
from django.urls import path, include
from chatapp_api.views import CustomObtainAuthTokenView, UserCreationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatapp.urls', namespace='chatapp')),
    path('api/', include('chatapp_api.urls', namespace='chatapp_api'))
]

urlpatterns += [
    path("api/", include("core.api_router")),
    path("auth-signup/", UserCreationView.as_view()),
    path("auth-token/", CustomObtainAuthTokenView.as_view()),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]