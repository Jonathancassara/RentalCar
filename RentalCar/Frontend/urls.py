from django.urls import path
from . import views

urlpatterns = [
    # Rental-related URLs
    path('rentals/', views.RentalListView.as_view(), name='rental_list'),  # List all rentals
    path('rentals/new/', views.CreateRentalView.as_view(), name='create_rental'),  # Create a new rental
    path('rentals/<int:pk>/update/', views.UpdateRentalView.as_view(), name='update_rental'),  # Update a rental (return car)
    path('rentals/<int:pk>/delete/', views.DeleteRentalView.as_view(), name='delete_rental'),  # Delete a rental

    # Driver-related URLs
    path('drivers/', views.DriverListView.as_view(), name='driver_list'),  # List all drivers
    path('drivers/new/', views.CreateDriverView.as_view(), name='create_driver'),  # Add a new driver

    # Car-related URLs
    path('cars/', views.CarListView.as_view(), name='car_list'),  # List all cars
    path('cars/new/', views.CreateCarView.as_view(), name='create_car'),  # Add a new car
]
