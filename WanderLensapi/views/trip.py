
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from WanderLensapi.models.trip import Trip
from WanderLensapi.models.triptype import TripType
from WanderLensapi.serializers.trip import TripSerializer


class TripView(ViewSet):
    """Trip view set"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized instance
        """
        new_trip = Trip()
        new_trip.user = request.auth.user
        new_trip.name = request.data["name"]
        new_trip.description = request.data["description"]
        new_trip.trip_type = TripType.objects.get(pk=request.data["trip_type_id"])
        new_trip.start_date = request.data["start_date"]
        new_trip.color = request.data.get("color", "#3B82F6")
        new_trip.is_private = request.data.get("is_private", False)

        try:
            new_trip.save()
            serializer = TripSerializer(new_trip)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         """Handle GET requests for single item

#         Returns:
#             Response -- JSON serialized instance
#         """
#         try:
#             void = Void.objects.get(pk=pk)
#             serializer = VoidSerializer(void)
#             return Response(serializer.data)
#         except Exception as ex:
#             return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk=None):
#         """Handle PUT requests

#         Returns:
#             Response -- Empty body with 204 status code
#         """
#         try:
#             void = Void.objects.get(pk=pk)
#             void.sample_name = request.data["name"]
#             void.sample_description = request.data["description"]
#             void.save()
#         except Void.DoesNotExist:
#             return Response(None, status=status.HTTP_404_NOT_FOUND)

#         except Exception as ex:
#             return HttpResponseServerError(ex)

#         return Response(None, status=status.HTTP_204_NO_CONTENT)

#     def destroy(self, request, pk=None):
#         """Handle DELETE requests for a single item

#         Returns:
#             Response -- 200, 404, or 500 status code
#         """
#         try:
#             void = Void.objects.get(pk=pk)
#             void.delete()
#             return Response(None, status=status.HTTP_204_NO_CONTENT)

#         except Void.DoesNotExist as ex:
#             return Response({message: ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

#         except Exception as ex:
#             return Response({message: ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def list(self, request):
#         """Handle GET requests for all items

#         Returns:
#             Response -- JSON serialized array
#         """
#         try:
#             voids = Void.objects.all()
#             serializer = VoidSerializer(voids, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as ex:
#             return HttpResponseServerError(ex)


# class VoidSerializer(serializers.ModelSerializer):
#     """JSON serializer"""

#     class Meta:
#         model = Void
#         fields = ( id, sample_name, sample_description, )

