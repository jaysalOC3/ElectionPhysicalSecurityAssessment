from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Assessment, UserAssessment, AssessmentQuestion, AssessmentResponse
from .forms import AssessmentForm, AssessmentResponseForm 

def index(request):
    assessments = Assessment.objects.all()  # Fetch all assessments
    # Add any other data you want to pass to the template

    context = {
        'assessments': assessments,
        # ... other context variables
    }
    return render(request, 'assessment_app/index.html', context)

@login_required
def create_assessment(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.created_by = request.user
            assessment.save()
            # Create UserAssessment for the owner
            UserAssessment.objects.create(user=request.user, assessment=assessment, role='owner')
            return redirect('assessment_detail', pk=assessment.pk)
    else:
        form = AssessmentForm()
    return render(request, 'assessment_app/create_assessment.html', {'form': form})

@login_required
def assessment_detail(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)
    user_assessment = get_object_or_404(UserAssessment, user=request.user, assessment=assessment)

    def can_perform(action):
        return user_assessment.role == 'owner' or user_assessment.has_permission(action)

    can_edit = can_perform('edit')
    can_submit = can_perform('submit')
    can_view_responses = can_perform('view_responses')

    questions = assessment.collection.questions.all()
    responses = AssessmentResponse.objects.filter(user_assessment=user_assessment) if can_view_responses else None

    context = {
        'assessment': assessment,
        'questions': questions,
        'responses': responses,
        'can_edit': can_edit,
        'can_submit': can_submit,
        'can_view_responses': can_view_responses,
    }

    return render(request, 'assessment_app/assessment_detail.html', context)

@login_required
def edit_assessment(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)
    user_assessment = get_object_or_404(UserAssessment, user=request.user, assessment=assessment)

    if not (user_assessment.role == 'owner' or user_assessment.has_permission('edit')):
        return redirect('assessment_detail', pk=assessment.pk)

    if request.method == 'POST':
        form = AssessmentForm(request.POST, instance=assessment)
        if form.is_valid():
            form.save()
            return redirect('assessment_detail', pk=assessment.pk)
    else:
        form = AssessmentForm(instance=assessment)
    return render(request, 'assessment_app/edit_assessment.html', {'form': form, 'assessment': assessment})

@login_required
def submit_assessment(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)
    user_assessment = get_object_or_404(UserAssessment, user=request.user, assessment=assessment)

    if not (user_assessment.role == 'owner' or user_assessment.has_permission('submit')):
        return redirect('assessment_detail', pk=assessment.pk)

    assessment.status = 'submitted'
    assessment.save()
    return redirect('assessment_detail', pk=assessment.pk)

@login_required
def answer_questions(request, assessment_pk, question_section=None):
    assessment = get_object_or_404(Assessment, pk=assessment_pk)
    user_assessment = get_object_or_404(UserAssessment, user=request.user, assessment=assessment)
    question_section_all = assessment.collection.questions.values_list('question_section', flat=True).distinct()
    # Filter questions based on the question_section if provided
    if question_section:
        questions = assessment.collection.questions.filter(question_section=question_section)
    else:
        # If question_section is not provided, redirect to the first available section
        first_section = question_section_all.first()
        if first_section:
            return redirect('answer_questions_section', assessment_pk=assessment_pk, question_section=first_section)
        else:
            # Handle the case when no questions are available
            questions = []

    if request.method == 'POST':
        forms = [AssessmentResponseForm(request.POST, question=q) for q in questions]
        if all(form.is_valid() for form in forms):
            for form, question in zip(forms, questions):
                response = form.save(commit=False)
                response.user_assessment = user_assessment
                response.assessment_question = question  # Assign the assessment_question
                response.save()
            return redirect('assessment_detail', pk=assessment.pk)
    else:
        forms = [AssessmentResponseForm(question=q) for q in questions]

    return render(request, 'assessment_app/answer_questions.html', {'assessment': assessment, 'forms': forms, 'sections': question_section_all})