from django.db import models
from django.contrib.auth.models import User
import django.db.utils

# Permission choices for UserAssessment roles
permissions = [
    ('owner', 'Owner'),           # Full access to all features and settings
    ('admin', 'Administrator'),   # Manage settings, users, and critical components without full ownership rights
    ('sitelead', 'Site Leader'),   # Access to create and modify responses
    ('analyst', 'Analyst'),       # Read-only access with the ability to run queries and generate reports
    ('collaborator', 'Collaborator'), # Access to specific projects or databases for collaboration without admin rights
    ('guest', 'Guest')            # Very limited access, possibly only to certain data views
]


def get_default_collection():
    # Try to get the first collection
    try:
        collection = AssessmentQuestionCollection.objects.first()
        if not collection:
            # No collection found, create a new default collection
            collection = AssessmentQuestionCollection.objects.create(
                name="Default Collection",
                description="Automatically created default collection"
            )
        return collection.id
    except django.db.utils.OperationalError:
        # This handles the case where this is called during a migration and the table doesn't exist yet
        return None

class AssessmentQuestionCollection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"
    
class AssessmentQuestion(models.Model):
    collection = models.ForeignKey(
        'AssessmentQuestionCollection',
        on_delete=models.CASCADE,
        related_name='questions',
        default=get_default_collection,
        null=True  # Allows the field to be null if no default collection is available at the time
    )
    question_text = models.TextField()
    question_help_text = models.TextField()
    question_type = models.CharField(max_length=50, choices=[
        ('multiple_choice', 'Multiple Choice'), 
        ('text', 'Text'), 
        ('checkbox', 'Checkbox')
    ])
    order = models.IntegerField()
    required = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.question_text[:50]}..."  # Return first 50 characters if long

class Assessment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('approved', 'Approved')])
    due_date = models.DateField(null=True, blank=True)
    collection = models.ForeignKey(
        'AssessmentQuestionCollection',
        on_delete=models.SET_NULL,
        related_name='assessments',
        null=True,  # Allows the field to be null
        default=get_default_collection,  # Set the default collection
        help_text="The collection used for this assessment."
    )

    def __str__(self):
        return self.name
    
class UserAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='user_assessments')
    role = models.CharField(max_length=50, choices=permissions)

    def __str__(self):
        return f"{self.user.username} - {self.assessment.name}"
    def has_permission(self, perm_name):
        return self.permissions.filter(permission_type=perm_name).exists()

class AssessmentResponse(models.Model):
    user_assessment = models.ForeignKey(UserAssessment, on_delete=models.CASCADE, related_name='responses')
    assessment_question = models.ForeignKey(AssessmentQuestion, on_delete=models.CASCADE, related_name='responses')
    response_text = models.TextField(blank=True)

    def __str__(self):
        return f"Response by {self.user_assessment.user.username} for question {self.assessment_question.question_text[:50]}"

class UserAssessmentPermission(models.Model):
    user_assessment = models.ForeignKey(UserAssessment, on_delete=models.CASCADE, related_name='permissions')
    permission_type = models.CharField(max_length=50, choices=[('view', 'View'), ('edit', 'Edit'), ('submit', 'Submit')])

    def __str__(self):
        return f"{self.permission_type} - {self.user_assessment.user.username}"
