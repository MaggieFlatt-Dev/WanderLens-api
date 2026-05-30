from django.db import models

from WanderLensapi.models.stop import Stop

class Photo(models.Model):
  stop = models.ForeignKey(Stop, related_name='photos', on_delete=models.CASCADE)
  image = models.ImageField(upload_to='stop_photos/')
  description = models.CharField(max_length=255, blank=True)
  