from django.db import models
from django.contrib.auth.models import User

class UserFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=[('usability', 'Usability'), ('functionality', 'Functionality'), ('bug_report', 'Bug Report')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feedback from {self.user.username}"
