from rest_framework import serializers
from WanderLensapi.models import TripType


class TripTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for TripType"""

    class Meta:
        model = TripType
        fields = ("id", "name", "is_custom")