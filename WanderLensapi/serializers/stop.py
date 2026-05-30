from WanderLensapi.models import Stop
from rest_framework import serializers

from WanderLensapi.serializers.category import CategorySerializer
from WanderLensapi.serializers.photo import PhotoSerializer


class StopSerializer(serializers.ModelSerializer):
    """JSON serializer for Stop"""

    categories = CategorySerializer(many=True, read_only=True)
    trip_name = serializers.CharField(source="trip.name", read_only=True)
    trip_color = serializers.CharField(source="trip.color", read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Stop
        fields = (
            "id",
            "name",
            "description",
            "city",
            "country",
            "latitude",
            "longitude",
            "visited_date",
            "categories",
            "trip_id",
            "trip_name",
            "trip_color",
            "photos",
        )
