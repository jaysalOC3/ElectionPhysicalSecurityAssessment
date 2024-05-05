from django.contrib import admin
from .models import Assessment, UserAssessment, AssessmentQuestion, AssessmentResponse, UserAssessmentPermission, AssessmentQuestionCollection

admin.site.register(Assessment)
admin.site.register(UserAssessment)
@admin.register(AssessmentQuestion)
class AssessmentQuestion(admin.ModelAdmin):
    list_display = ('collection', 'question_text')

@admin.register(AssessmentQuestionCollection)
class AssessmentQuestionCollection(admin.ModelAdmin):
    list_display = ('name', 'is_active')

admin.site.register(AssessmentResponse)
admin.site.register(UserAssessmentPermission)
