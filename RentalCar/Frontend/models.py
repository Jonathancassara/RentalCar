from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=50)  # Driver's first name
    surname = models.CharField(max_length=50)  # Driver's last name
    email = models.EmailField(max_length=100, unique=True)  # Unique email
    phone_number = models.CharField(max_length=15, unique=True)  # Unique phone number

    def __str__(self):
        return f"{self.name} {self.surname}"


class Car(models.Model):
    make = models.CharField(max_length=50)  # Car make (e.g., Toyota)
    model = models.CharField(max_length=100)  # Car model (e.g., Corolla)
    registration_number = models.CharField(max_length=10, unique=True)  # Unique registration number
    is_available = models.BooleanField(default=True)  # Tracks availability for rental

    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # Link to Car
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)  # Link to Driver
    rent_date = models.DateTimeField()  # Rental start date
    return_date = models.DateTimeField(null=True, blank=True)  # Optional return date
    comments = models.TextField(blank=True, null=True)  # Optional comments

    def save(self, *args, **kwargs):
        """
        Override save method to manage car availability:
        - If the rental is returned (return_date set), mark the car as available.
        - If the rental is ongoing (return_date not set), mark the car as unavailable.
        """
        if self.return_date:
            self.car.is_available = True  # Car is available after return
        else:
            self.car.is_available = False  # Car is unavailable during rental
        self.car.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Override delete method to mark the car as available when a rental is deleted.
        """
        self.car.is_available = True
        self.car.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Rental of {self.car} by {self.driver} on {self.rent_date}"
