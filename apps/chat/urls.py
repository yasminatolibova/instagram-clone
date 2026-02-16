# chat/urls.py
from django.urls import path
from .views import (
    ChatListAPIView,
    MessageListAPIView,
    SendMessageAPIView,
    CreateChatAPIView
)

urlpatterns = [
    path('chats/', ChatListAPIView.as_view()),
    path('chats/create/', CreateChatAPIView.as_view()),
    path('chats/<int:room_id>/messages/', MessageListAPIView.as_view()),
    path('chats/<int:room_id>/send/', SendMessageAPIView.as_view()),
]
