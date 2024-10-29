# paragraph_generator/models.py
from django.db import models
from django.contrib.auth.models import User

class GeneratedContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField()
    content = models.TextField()
    word_count = models.IntegerField()
    topic = models.CharField(max_length=200)
    grade_level = models.CharField(max_length=50)
    tone = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Content by {self.user.username} at {self.created_at}"

class UserApiUsage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_usage = models.IntegerField(default=0)
    last_reset = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"API usage for {self.user.username}"