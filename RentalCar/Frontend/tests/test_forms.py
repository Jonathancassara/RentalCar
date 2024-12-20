from django.test import TestCase
from Frontend.forms import RentalForm
from Frontend.models import Driver, Car
from datetime import datetime

class RentalFormTests(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            name="John",
            surname="Doe",
            email="john@example.com",
            phone_number="1234567890"
        )
        self.car = Car.objects.create(
            make="Toyota",
            model="Corolla",
            registration_number="ABC123"
        )

    def test_rental_form_valid(self):
        form = RentalForm(data={
            'car': self.car.id,
            'driver': self.driver.id,
            'rent_date': datetime.now()
        })
        self.assertTrue(form.is_valid())

    def test_rental_form_invalid_car(self):
        # Create an existing rental to make the car unavailable
        self.car.is_available = False
        self.car.save()
        form = RentalForm(data={
            'car': self.car.id,
            'driver': self.driver.id,
            'rent_date': datetime.now()
        })
        self.assertFalse(form.is_valid())
        self.assertIn('car', form.errors)
