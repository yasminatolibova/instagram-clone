from django.db import models
from django.contrib.auth.models import User
from ..posts.models import Post
from ..reels.models import Reel
from ..story.models import Story

# Create your models here.
class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments', blank=True, null=True)
    reels=models.ForeignKey(Reel, on_delete=models.CASCADE, related_name='reels_comments', blank=True, null=True)
    story=models.ForeignKey(Story, on_delete=models.CASCADE, related_name='story_comments', blank=True, null=True)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user}"
    

class CommentLike(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    created_at=models.DateTimeField(auto_now_add=True)

