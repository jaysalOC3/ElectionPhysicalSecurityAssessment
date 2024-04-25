from django.db import models
from django.contrib.auth.models import User

class Assessment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('approved', 'Approved')])
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class UserAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('owner', 'Owner'), ('collaborator', 'Collaborator')])

class AssessmentQuestion(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(max_length=50, choices=[('multiple_choice', 'Multiple Choice'), ('text', 'Text'), ('checkbox', 'Checkbox')])
    order = models.IntegerField()
    required = models.BooleanField(default=True)

class AssessmentResponse(models.Model):
    user_assessment = models.ForeignKey(UserAssessment, on_delete=models.CASCADE)
    assessment_question = models.ForeignKey(AssessmentQuestion, on_delete=models.CASCADE)
    response_text = models.TextField(blank=True)
    # Add response_option if needed for multiple-choice questions

class UserAssessmentPermission(models.Model):
    user_assessment = models.ForeignKey(UserAssessment, on_delete=models.CASCADE)
    permission_type = models.CharField(max_length=50, choices=[('view', 'View'), ('edit', 'Edit'), ('submit', 'Submit')])