from WanderLensapi.models import Stop
from rest_framework import serializers

from WanderLensapi.serializers.category import CategorySerializer


class StopSerializer(serializers.ModelSerializer):
    """JSON serializer for Stop"""

    categories = CategorySerializer(many=True, read_only=True)
    trip_name = serializers.CharField(source="trip.name", read_only=True)
    trip_color = serializers.CharField(source="trip.color", read_only=True)

    class Meta:
        model = Stop
        fields = (
            "id",
            "trip_id",
            "trip_name",
            "trip_color",
            "name",
            "description",
            "city",
            "country",
            "latitude",
            "longitude",
            "visited_date",
            "categories",
        )
