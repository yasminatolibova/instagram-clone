from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"
    


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts.Like.user+')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts.Like.user+')

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} likes {self.post.id}"
    

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts.Comment.user+')
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts.Comment.user+')
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"{self.user.username} commented on {self.post.id}"