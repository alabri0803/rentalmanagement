from django.urls import path

from . import views

app_name = 'properties'

urlpatterns = [
  path('', views.PropertyListView.as_view(), name='property_list'),
  path('add/', views.PropertyCreateView.as_view(), name='property_add'),
  path('<int:pk>/', views.PropertyDetailView.as_view(), name='property_detail'),
  path('<int:property_id>/add-unit/', views.UnitCreateView.as_view(), name='unit_add'),
]