from django.db import models
from django.contrib.auth.models import User

class Reel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reels')
    video = models.FileField(upload_to='reels/videos/')
    caption = models.TextField(blank=True)
    views_count=models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='liked_reels', blank=True)
    is_public = models.BooleanField(default=True)
    tags = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Teglar",
        help_text="Vergul bilan ajratilgan"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} is the author"



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reels.Like.user+')
    reel = models.ForeignKey(Reel, on_delete=models.CASCADE, related_name='reels.Like.user+')

    class Meta:
        unique_together = ('user', 'reel')

    def __str__(self):
        return f"{self.user.username} likes {self.reel.id}"
    

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reels.Comment.user+')
#     reel = models.ForeignKey(Reel, on_delete=models.CASCADE, related_name='reels.Comment.user+')
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"{self.user.username} commented on {self.reel.id}"