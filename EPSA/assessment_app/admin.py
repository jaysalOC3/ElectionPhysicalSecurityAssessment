from django.contrib import admin
from .models import Assessment, UserAssessment, AssessmentQuestion, AssessmentResponse, UserAssessmentPermission

admin.site.register(Assessment)
admin.site.register(UserAssessment)
admin.site.register(AssessmentQuestion)
admin.site.register(AssessmentResponse)
admin.site.register(UserAssessmentPermission)
