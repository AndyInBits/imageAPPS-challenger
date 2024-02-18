from django.urls import path

from . import views

urlpatterns = [
    path("healthcheck", views.HealthCheck.as_view(), name="healthcheck"),
    path('client/<int:client_id>/packages/', views.ClientPackagesView.as_view(), name='client_packages'),
    path('carrier/<int:carrier_id>/packages/', views.CarrierPackagesView.as_view(), name='carrier_packages'),
    path('package/create/', views.CreatePackageView.as_view(), name='create_package'),
    path('package/<int:pk>/', views.PackageDetailsView.as_view(), name='package_details'),
    path('packages/', views.PackageListView.as_view(), name='package_list'),
    path('package/<int:pk>/edit/', views.EditPackageView.as_view(), name='edit_package'),
    path('package/<int:pk>/delete/', views.DeletePackageView.as_view(), name='delete_package'),
    path('api/assign_carrier/', views.AssignCarrierView.as_view(), name='assign_carrier'),







]