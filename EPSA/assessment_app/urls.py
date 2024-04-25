from django.urls import path
from . import views

urlpatterns = [
    path('assessments/create/', views.create_assessment, name='create_assessment'),
    path('assessments/<int:pk>/', views.assessment_detail, name='assessment_detail'),
    path('assessments/<int:pk>/edit/', views.edit_assessment, name='edit_assessment'),
    path('assessments/<int:pk>/submit/', views.submit_assessment, name='submit_assessment'),
    path('assessments/<int:assessment_pk>/answer/', views.answer_questions, name='answer_questions'),
]