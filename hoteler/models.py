import uuid
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    price = models.IntegerField(default=100)  # ← Add a default here

    def __str__(self):
        return self.name


class Guest(models.Model):
    guest_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.guest_name


class Reservation(models.Model):
    hotel_name = models.CharField(max_length=100)
    checkin = models.CharField(max_length=50)
    checkout = models.CharField(max_length=50)
    guests = models.ManyToManyField(Guest)
    confirmation_number = models.CharField(
        max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.confirmation_number:
            self.confirmation_number = str(uuid.uuid4())[
                :8].upper()  # e.g. '9F4C2A1D'
        super().save(*args, **kwargs)
