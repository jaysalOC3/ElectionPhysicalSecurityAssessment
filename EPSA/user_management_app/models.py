from django.db import models
from django.contrib.auth.models import User

class UserRole(models.Model):
    name = models.CharField(max_length=50)  # e.g., admin, analyst, collaborator

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)  # For nested comments
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NotificationPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=50, choices=[('email', 'Email'), ('sms', 'SMS'), ('push', 'Push Notification')]) 
    frequency = models.CharField(max_length=50, choices=[('immediate', 'Immediate'), ('daily', 'Daily'), ('weekly', 'Weekly')])