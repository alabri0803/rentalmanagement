from django.urls import path

from . import views

app_name = 'tenants'

urlpatterns = [
  path('', views.TenantListView.as_view(), name='tenant_list'),
  path('<int:pk>/', views.TenantDetailView.as_view(), name='tenant_detail'),
  path('add/', views.TenantCreateView.as_view(), name='tenant_add'),
  path('<int:pk>/edit/', views.TenantUpdateView.as_view(), name='tenant_edit'),
  path('<int:pk>/delete/', views.TenantDeleteView.as_view(), name='tenant_delete')
]