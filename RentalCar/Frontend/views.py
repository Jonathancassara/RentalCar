from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Rental, Driver, Car
from django.http import JsonResponse
from .forms import RentalForm, DriverForm, CarForm  # Assume you have created these forms
from datetime import datetime
import logging
logger = logging.getLogger(__name__)

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
    fields = ['car', 'driver', 'rent_date', 'return_date', 'comments']
    template_name = 'Frontend/rental_form.html'
    success_url = reverse_lazy('rental_list')

    def post(self, request, *args, **kwargs):
        logger.info("POST data: %s", request.POST)
        return super().post(request, *args, **kwargs)
        try:
            # Parse return_date from the request
            return_date = request.POST.get('return_date')
            if return_date:
                rental.return_date = datetime.strptime(return_date, '%Y-%m-%dT%H:%M')
            else:
                return JsonResponse({'error': 'Return date is required'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Invalid return date format'}, status=400)

        # Update the comment (optional field)
        rental.comments = request.POST.get('comments', rental.comments)
        rental.save()
        return redirect(self.success_url)

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
    
class FinishRentalView(UpdateView):
    model = Rental
    fields = ['return_date', 'comments']
    success_url = reverse_lazy('rental_list')
    template_name = 'Frontend/rental_form.html'

    def post(self, request, *args, **kwargs):
        rental = get_object_or_404(Rental, pk=kwargs['pk'])
        rental.return_date = request.POST.get('return_date')
        rental.comments = request.POST.get('comments', rental.comments)
        rental.save()
        return redirect(self.success_url)

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