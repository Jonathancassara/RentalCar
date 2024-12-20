from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Rental, Driver, Car
from .forms import RentalForm, DriverForm, CarForm  # Assume you have created these forms

def index(request):
    return render(request, 'Frontend/index.html')

def home(request):
    return render(request, 'Frontend/home.html')

# Rental Views
class RentalListView(ListView):
    model = Rental
    template_name = 'Frontend/rental_list.html'
    context_object_name = 'rentals'

    def get_queryset(self):
        return Rental.objects.select_related('car', 'driver').all()

class CreateRentalView(CreateView):
    model = Rental
    form_class = RentalForm
    template_name = 'Frontend/rental_form.html'
    success_url = reverse_lazy('rental_list')

    def form_valid(self, form):
        rental = form.save(commit=False)
        # Ensure the car is marked as unavailable
        rental.car.is_available = False
        rental.car.save()
        return super().form_valid(form)

class UpdateRentalView(UpdateView):
    model = Rental
    form_class = RentalForm
    template_name = 'Frontend/rental_form.html'
    success_url = reverse_lazy('rental_list')

    def form_valid(self, form):
        # Save the rental and include comments
        rental = form.save(commit=False)
        rental.comments = form.cleaned_data.get('comments')  # Ensure comments are saved
        rental.save()
        return super().form_valid(form)

class DeleteRentalView(DeleteView):
    model = Rental
    template_name = 'Frontend/rental_confirm_delete.html'
    success_url = reverse_lazy('rental_list')

    def delete(self, request, *args, **kwargs):
        rental = self.get_object()
        # Mark the car as available before deleting the rental
        rental.car.is_available = True
        rental.car.save()
        return super().delete(request, *args, **kwargs)

# Driver Views
class DriverListView(ListView):
    model = Driver
    template_name = 'Frontend/driver_list.html'
    context_object_name = 'drivers'
class CreateDriverView(CreateView):
    model = Driver
    form_class = DriverForm  # Use custom form with validation
    template_name = 'Frontend/driver_form.html'
    success_url = reverse_lazy('driver_list')

class UpdateDriverView(UpdateView):
    model = Driver
    form_class = DriverForm
    template_name = 'Frontend/driver_form.html'
    success_url = reverse_lazy('driver_list')

class DeleteDriverView(DeleteView):
    model = Driver
    template_name = 'Frontend/driver_confirm_delete.html'
    success_url = reverse_lazy('driver_list')

# Car Views
class CarListView(ListView):
    model = Car
    template_name = 'Frontend/car_list.html'
    context_object_name = 'cars'

class CreateCarView(CreateView):
    model = Car
    fields = ['make', 'model', 'registration_number']
    success_url = reverse_lazy('car_list')

class UpdateCarView(UpdateView):
    model = Car
    fields = ['make', 'model', 'registration_number']
    template_name = 'Frontend/car_form.html'  # Custom template for editing cars
    success_url = reverse_lazy('car_list')  # Redirect to the car list after updating

class DeleteCarView(DeleteView):
    model = Car
    template_name = 'Frontend/car_confirm_delete.html'  # Custom confirmation template
    success_url = reverse_lazy('car_list')  # Redirect to the cars list after deletion