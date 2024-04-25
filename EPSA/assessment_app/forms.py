from django import forms
from .models import Assessment, AssessmentResponse

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['name', 'description', 'status', 'due_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'due_date': forms.DateInput(attrs={'type': 'date'}), 
        }

class AssessmentResponseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        
        # Customize field based on question type
        if self.question.question_type == 'multiple_choice':
            choices = [(o.pk, o.option_text) for o in self.question.options.all()]
            self.fields['response_text'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
        elif self.question.question_type == 'checkbox':
            choices = [(o.pk, o.option_text) for o in self.question.options.all()]
            self.fields['response_text'] = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = AssessmentResponse
        fields = ['response_text']
        widgets = {
            'response_text': forms.Textarea(attrs={'rows': 2})  # Default widget for text questions
        }
