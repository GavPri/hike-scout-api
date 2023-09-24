from django.db import models
from posts.models import Posts
from django.contrib.auth.models import User


class Comments(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=255, blank=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.content