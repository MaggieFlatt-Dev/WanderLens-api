from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from WanderLensapi.models import TripType
from WanderLensapi.serializers.triptype import TripTypeSerializer


class TripTypeView(ViewSet):
    """TripType view"""

    def list(self, request):
        """Handle GET requests for TripType

        Returns:
            Response -- JSON serialized list of TripTypes
        """
        try:
            trip_types = TripType.objects.all()
            serializer = TripTypeSerializer(trip_types, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)