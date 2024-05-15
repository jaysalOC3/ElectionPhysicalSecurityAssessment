from django.urls import path
from . import views

urlpatterns = [
    path('risk-landscape-data/', views.risk_landscape_data, name='risk_landscape_data'),
]