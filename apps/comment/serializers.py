from rest_framework import serializers
from ..accounts.serializers import UserSerializer
from .models import Comment



class CommentSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    likes_count=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields='__all__'
    def get_likes_count(self, obj):
        return obj.likes.count()
