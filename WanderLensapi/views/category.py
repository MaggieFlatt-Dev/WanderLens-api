from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from WanderLensapi.models import Category
from WanderLensapi.serializers.category import CategorySerializer


class CategoryView(ViewSet):
    """Category view"""

    def list(self, request):
        """Handle GET requests for Category

        Returns:
            Response -- JSON serialized list of Categories
        """
        try:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)