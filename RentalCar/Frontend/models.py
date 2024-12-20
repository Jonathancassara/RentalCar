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
    is_available = models.BooleanField(default=True)  # Tracks if the car is available for rent

    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rent_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if self.return_date:  # Car is returned
            self.car.is_available = True
        else:  # Car is rented
            self.car.is_available = False
        self.car.save()
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        # Mark the car as available when a rental is deleted
        self.car.is_available = True
        self.car.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Rental of {self.car} by {self.driver} on {self.rent_date}"
