from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Story
from ..accounts.serializers import UserSerializer


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']


class StorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    views_count = serializers.SerializerMethodField()
    viewed_users = serializers.SerializerMethodField()


    class Meta:
        model = Story
        fields = ['id', 'user', 'image', 'video', 'caption', 'is_public', 'created_at', 'likes_count', 'views_count', 'viewed_users',  'is_active']
    

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_views_count(self, obj):
        return obj.views.count()

    def get_viewed_users(self, obj):
        return UserSerializer(obj.views.all(), many=True).data
        

    

# class CommentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Comment
#         fields = ['id', 'user', 'story', 'text', 'created_at']