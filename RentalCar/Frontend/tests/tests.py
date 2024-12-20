from django.test import TestCase
from django.utils.timezone import now
from Frontend.forms import RentalForm
from Frontend.models import Driver, Car

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
            'rent_date': now()  # Use timezone-aware datetime
        })
        self.assertTrue(form.is_valid())
