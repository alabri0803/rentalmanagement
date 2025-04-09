from django.urls import path

from . import views

app_name = 'properties'

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('add/', views.add_property, name='add_property'),
    path('<int:pk>/', views.property_detail, name='property_detail'),
    path('<int:property_id>/unit/add/', views.add_unit, name='add_unit')
]