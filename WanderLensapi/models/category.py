from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    is_custom = models.BooleanField(default=False)

    created_by_user_id = models.IntegerField(null=True, blank=True)
