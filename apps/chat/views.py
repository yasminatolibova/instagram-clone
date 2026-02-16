from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer
from django.contrib.auth.models import User


class ChatListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        chats = ChatRoom.objects.filter(users=request.user)
        serializer = ChatRoomSerializer(chats, many=True)
        return Response(serializer.data)
class MessageListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, room_id):
        messages = Message.objects.filter(room_id=room_id)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
class SendMessageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, room_id):
        text = request.data.get('text')

        message = Message.objects.create(
            room_id=room_id,
            sender=request.user,
            text=text
        )

        serializer = MessageSerializer(message)
        return Response(serializer.data)
class CreateChatAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user_id')
        other_user = User.objects.get(id=user_id)

        room = ChatRoom.objects.filter(users=request.user).filter(users=other_user).first()

        if not room:
            room = ChatRoom.objects.create()
            room.users.add(request.user, other_user)

        serializer = ChatRoomSerializer(room)
        return Response(serializer.data)
