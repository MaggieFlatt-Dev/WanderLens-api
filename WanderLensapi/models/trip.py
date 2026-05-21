"""User Trip model"""

from django.conf import settings
from django.db import models
from .triptype import TripType


class Trip(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="trips",
    )
    trip_type = models.ForeignKey(
        TripType,
        on_delete=models.PROTECT,
        related_name="trips",
    )
    name = models.CharField(max_length=150)

    description = models.TextField(blank=True)

    color = models.CharField(max_length=7, default="#3B82F6")

    start_date = models.DateField()

    is_private = models.BooleanField(default=False)
