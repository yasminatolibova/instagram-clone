# chat/serializers.py
from rest_framework import serializers
from .models import ChatRoom, Message
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'text', 'is_read', 'created_at']


class ChatRoomSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = ChatRoom
        fields = ['id', 'users', 'last_message']

    def get_last_message(self, obj):
        message = obj.messages.order_by('-created_at').first()
        if message:
            return MessageSerializer(message).data
        return None
