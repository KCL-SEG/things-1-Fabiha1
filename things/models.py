from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(Model):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.TextField(unique=False, blank=True, max_length=120)
    quantity = models.IntegerField(
        unique=False, 
        validators=[
            MinValueValidator(0, message="Quantity cannot be less than 0"),
            MaxValueValidator(100, message="Quantity cannot be more than 100")
        ]
    )

        
