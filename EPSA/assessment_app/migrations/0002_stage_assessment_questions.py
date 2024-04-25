from django.db import migrations
from assessment_app.models import AssessmentQuestion, Assessment

class Migration(migrations.Migration):
    dependencies = [
        ('assessment_app', '0001_initial'),  # Replace with the appropriate migration dependency
    ]

    def forwards(apps, schema_editor):
        # Get the Assessment model
        Assessment = apps.get_model('assessment_app', 'Assessment')
        
        # Create or retrieve the desired Assessment instance
        assessment = Assessment.objects.get_or_create(name='Your Assessment')[0]
        
        # Create AssessmentQuestion instances
        questions = [
            AssessmentQuestion(
                assessment=assessment,
                question_text='Question 1',
                question_type='multiple_choice',
                order=1,
                required=True
            ),
            AssessmentQuestion(
                assessment=assessment,
                question_text='Question 2',
                question_type='text',
                order=2,
                required=False
            ),
            # Add more questions as needed
        ]
        
        # Bulk create the AssessmentQuestion instances
        AssessmentQuestion.objects.bulk_create(questions)

    def backwards(apps, schema_editor):
        # Get the AssessmentQuestion model
        AssessmentQuestion = apps.get_model('assessment_app', 'AssessmentQuestion')
        
        # Delete the staged AssessmentQuestion instances
        AssessmentQuestion.objects.filter(assessment__name='Your Assessment').delete()