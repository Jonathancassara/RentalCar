from django import forms
from .models import Rental, Driver, Car

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['car', 'driver', 'rent_date', 'return_date', 'comments']
        widgets = {
            'car': forms.Select(attrs={'class': 'form-control'}),
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'rent_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'value': '',  # This will be set dynamically via JavaScript
            }),
            'return_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add comments here'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(is_available=True)

    def clean_car(self):
        """
        Ensure the selected car is available before saving the rental.
        """
        car = self.cleaned_data['car']
        if not car.is_available:
            raise forms.ValidationError(f"The car '{car}' is not available.")
        return car


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'surname', 'email', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'registration_number']
        widgets = {
            'make': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Car Make'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Car Model'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registration Number'}),
        }
