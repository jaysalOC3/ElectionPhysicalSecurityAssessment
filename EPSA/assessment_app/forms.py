from django import forms
from .models import Assessment, AssessmentResponse

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['name', 'collection', 'description', 'status', 'due_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'due_date': forms.DateInput(attrs={'type': 'date'}), 
        }

class AssessmentResponseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        if self.question:
            self.fields['response_text'].label = self.question.question_text
            self.fields['response_text'].help_text  = self.question.question_help_text
    class Meta:
        model = AssessmentResponse
        fields = ['response_text']
        widgets = {
            'response_text': forms.Textarea(attrs={'rows': 2})  # Default widget for text questions
        }
