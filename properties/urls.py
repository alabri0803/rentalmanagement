from django.urls import path

from . import views

app_name = 'properties'

urlpatterns = [
    path('', views.PropertyListView.as_view(), name='property_list'),
    path('<int:pk>/', views.PropertyDetailView.as_view(), name='property_detail'),
    path('add/', views.PropertyCreateView.as_view(), name='property_add'),
    path('<int:pk>/edit/', views.PropertyUpdateView.as_view(), name='property_edit'),
    path('<int:pk>/delete/', views.PropertyDeleteView.as_view(), name='property_delete'),
    path('<int:pk>/upload-image/', views.PropertyImageUploadView.as_view(), name='property_upload_image'),
    path('<int:property_id>/units/add/', views.UnitCreateView.as_view(), name='unit_add'),
    path('units/<int:pk>/edit/', views.UnitUpdateView.as_view(), name='unit_edit'),
    path('units/<int:pk>/delete/', views.UnitDeleteView.as_view(), name='unit_delete'),
]