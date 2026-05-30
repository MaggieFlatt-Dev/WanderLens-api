from rest_framework import serializers

from WanderLensapi.models.photo import Photo

class PhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for Photo"""

    class Meta:
        model = Photo
        fields = ['id', 'image', 'description']