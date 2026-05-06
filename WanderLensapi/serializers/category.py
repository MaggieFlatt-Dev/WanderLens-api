from rest_framework import serializers
from WanderLensapi.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for Category"""

    class Meta:
        model = Category
        fields = ("id", "name", "is_custom", "created_by_user_id")