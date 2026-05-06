from WanderLensapi.models.trip import Trip
from rest_framework import serializers


class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for Trip"""

    class Meta:
        model = Trip
        fields = (
            "id", 
            "user_id", "trip_type_id", 
            "name", 
            "description", "start_date")
