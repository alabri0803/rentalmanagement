from django.urls import path

from . import views

urlpatterns = [
  path('', views.property_list, name='property_list'),
  path('<int:pk>/', views.property_detail, name='property_detail'),
  path('add/', views.property_create, name='property_create'),
]