from WanderLensapi.models import Trip
from rest_framework import serializers

from WanderLensapi.serializers.stop import StopSerializer


class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for Trip"""

    stops = StopSerializer(many=True, read_only=True, source="stop_set")

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
            "stops",
        )
        depth = 1
