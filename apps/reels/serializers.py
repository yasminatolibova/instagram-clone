from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Reel, Like
from ..accounts.serializers import UserSerializer
# from ..posts.serializers import CommentSerializer

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']


class ReelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Reel
        fields = ['id', 'user', 'video', 'caption', 'views_count', 'tags', 'is_public', 'created_at', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()
    

# class CommentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Comment
#         fields = ['id', 'user', 'reel', 'text', 'created_at']