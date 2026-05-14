
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

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized instance
        """
        try:
            trip = Trip.objects.get(pk=pk, user=request.auth.user)
            serializer = TripSerializer(trip)
            return Response(serializer.data)
        except Trip.DoesNotExist:
            return Response({"reason": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """Handle PATCH requests

        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            trip = Trip.objects.get(pk=pk, user=request.auth.user)
            if "name" in request.data:
                trip.name = request.data["name"]
            if "description" in request.data:
                trip.description = request.data["description"]
            if "trip_type_id" in request.data:
                trip.trip_type = TripType.objects.get(pk=request.data["trip_type_id"])
            if "start_date" in request.data:
                trip.start_date = request.data["start_date"]
            if "color" in request.data:
                trip.color = request.data["color"]
            if "is_private" in request.data:
                trip.is_private = request.data["is_private"]
            trip.save()
        except Trip.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return HttpResponseServerError(ex)

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single item

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            trip = Trip.objects.get(pk=pk, user=request.auth.user)
            trip.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        except Trip.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests for all items

        Returns:
            Response -- JSON serialized array
        """
        try:
            trips = Trip.objects.filter(user=request.auth.user).order_by("-start_date")
            serializer = TripSerializer(trips, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

