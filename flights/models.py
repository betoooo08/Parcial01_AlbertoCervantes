from django.db import models

class Flight(models.Model):
    class FlightType(models.TextChoices):
        NATIONAL = 'NAC', 'Nacional'
        INTERNATIONAL = 'INT', 'Internacional'

    name  = models.CharField(max_length=100)
    type  = models.CharField(max_length=3, choices=FlightType.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()}) - ${self.price}"