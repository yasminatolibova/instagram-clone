from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils import timezone
from  datetime import timedelta
from django.core.exceptions import ValidationError

class Story(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    image=models.ImageField(upload_to='stories/images/', blank=True, null=True)
    video=models.FileField(upload_to='stories/videos/', blank=True, null=True)
    caption=models.TextField(blank=True)
    views=models.ManyToManyField(User, related_name='viewed_stories', blank=True)
    likes = models.ManyToManyField(User, related_name='liked_stories', blank=True)
    is_public=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(hours=24)
    
    def clean(self):
        if not self.image and not self.video:
            raise ValidationError("Storyda rasm yoki video bulishi kerak.")

        if self.image and self.video:
            raise ValidationError("Storyda faqat bitta media bulishi mumkin.")


    def __str__(self):
        return f"{self.user.username}"
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories.Like.user+')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='stories.Like.user+')

    class Meta:
        unique_together = ('user', 'story')

    def __str__(self):
        return f"{self.user.username} likes {self.story.id}"
    

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories.Comment.user+')
#     story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='stories.Comment.user+')
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} commented on {self.story.id}"