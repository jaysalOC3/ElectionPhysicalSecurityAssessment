from django.contrib import admin
from .models import Assessment, UserAssessment, AssessmentQuestion, AssessmentResponse, UserAssessmentPermission, AssessmentQuestionCollection

admin.site.register(Assessment)
admin.site.register(UserAssessment)
admin.site.register(AssessmentQuestion)
admin.site.register(AssessmentResponse)
admin.site.register(UserAssessmentPermission)

admin.site.register(AssessmentQuestionCollection)
