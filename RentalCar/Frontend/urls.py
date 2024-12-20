from django.urls import path
from . import views

urlpatterns = [
    # Rental-related URLs
    path('', views.home, name='home'),
    path('list/', views.RentalListView.as_view(), name='rental_list'),  # List all rentals
    path('new/', views.CreateRentalView.as_view(), name='create_rental'),  # Create a new rental
    path('<int:pk>/update/', views.UpdateRentalView.as_view(), name='update_rental'),  # Update a rental (return car)
    path('<int:pk>/delete/', views.DeleteRentalView.as_view(), name='delete_rental'),  # Delete a rental

    # Driver-related URLs
    path('drivers/', views.DriverListView.as_view(), name='driver_list'),  # List all drivers
    path('drivers/new/', views.CreateDriverView.as_view(), name='create_driver'),  # Add a new driver
    path('drivers/<int:pk>/update/', views.UpdateDriverView.as_view(), name='update_driver'),
    path('drivers/<int:pk>/delete/', views.DeleteDriverView.as_view(), name='delete_driver'),

    # Car-related URLs
     path('cars/', views.CarListView.as_view(), name='car_list'),
    path('cars/new/', views.CreateCarView.as_view(), name='create_car'),
    path('cars/<int:pk>/update/', views.UpdateCarView.as_view(), name='update_car'),
    path('cars/<int:pk>/delete/', views.DeleteCarView.as_view(), name='delete_car'),

]
