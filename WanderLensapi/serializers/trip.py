from WanderLensapi.models import Trip
from rest_framework import serializers


class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for Trip"""

    class Meta:
        model = Trip
        fields = (
            "id", 
            "user_id", 
            "trip_type", 
            "name", 
            "description", 
            "start_date",
            "is_private",
            "color",
        )
        depth = 1
