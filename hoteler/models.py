from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
