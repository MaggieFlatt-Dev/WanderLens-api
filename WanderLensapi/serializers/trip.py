from WanderLensapi.models.trip import Trip
from rest_framework import serializers


class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for Trip"""

    class Meta:
        model = Trip
        fields = ("id", "name", "description")
        depth = 1

