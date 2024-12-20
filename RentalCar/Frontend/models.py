from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=50)  # Name: text, max 50 chars, not null
    surname = models.CharField(max_length=50)  # Surname: text, max 50 chars, not null
    email = models.EmailField(max_length=100)  # Email: text, max 100 chars, not null
    phone_number = models.CharField(max_length=50)  # PhoneNumber: text, max 50 chars, not null

    def __str__(self):
        return f"{self.name} {self.surname}"


class Car(models.Model):
    make = models.CharField(max_length=50)  # Make: text, max 50 chars, not null
    model = models.CharField(max_length=100)  # Model: text, max 100 chars, not null
    registration_number = models.CharField(max_length=10, unique=True)  # RegistrationNumber: text, max 10 chars, not null

    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # CarId: foreign key to Cars table
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)  # DriverId: foreign key to Drivers table
    rent_date = models.DateTimeField()  # RentDate: date time, not null
    return_date = models.DateTimeField(null=True, blank=True)  # ReturnDate: date time, nullable
    comments = models.TextField(blank=True)  # Comments: text, no length specified, nullable

    def __str__(self):
        return f"Rental of {self.car} by {self.driver} on {self.rent_date}"
