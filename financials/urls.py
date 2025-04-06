from django.urls import path

from . import views

urlpatterns = [
    path('summary/', views.financial_summary, name='financial_summary'),
]