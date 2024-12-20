from django.test import TestCase
from Frontend.models import Driver, Car, Rental
from datetime import datetime

class ModelTests(TestCase):
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

    def test_driver_creation(self):
        self.assertEqual(self.driver.name, "John")
        self.assertEqual(self.driver.surname, "Doe")
        self.assertEqual(self.driver.email, "john@example.com")
        self.assertEqual(self.driver.phone_number, "1234567890")

    def test_car_creation(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "Corolla")
        self.assertEqual(self.car.registration_number, "ABC123")
        self.assertTrue(self.car.is_available)
