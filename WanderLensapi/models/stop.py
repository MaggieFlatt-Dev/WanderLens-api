from django.db import models


class Stop(models.Model):
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    visited_date = models.DateField()
    categories = models.ManyToManyField("Category")