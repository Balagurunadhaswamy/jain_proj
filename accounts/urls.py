from django.urls import path
from .views import LoginAPIView, LogoutAPIView, RegisterView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name =  "accounts"

urlpatterns = [
    # path('register/', register_user, name='register'),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
    path('register/',RegisterView.as_view(),name="register"),
    path('login/',LoginAPIView.as_view(),name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]