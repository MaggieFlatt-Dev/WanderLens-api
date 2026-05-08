from WanderLensapi.models import Stop
from rest_framework import serializers


class StopSerializer(serializers.ModelSerializer):
    """JSON serializer for Stop"""

    class Meta:
        model = Stop
        fields = (
            "id", 
            "trip", 
            "name", 
            "description", 
            "city", 
            "country",
            "latitude",
            "longitude",
            "visited_date",
        )
        depth = 1
