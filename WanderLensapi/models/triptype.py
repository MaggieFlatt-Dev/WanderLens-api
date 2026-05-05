""" Trip Type model"""

from django.db import models

class TripType(models.Model):
  
    name = models.CharField(max_length=30, unique=True)