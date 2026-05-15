
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from WanderLensapi.models.category import Category
from WanderLensapi.models.stop import Stop
from WanderLensapi.models.trip import Trip
from WanderLensapi.serializers.stop import StopSerializer


class StopView(ViewSet):
    """Stop view set"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized instance
        """
        new_stop = Stop()
        new_stop.trip = Trip.objects.get(pk=request.data["trip_id"])
        new_stop.name = request.data["name"]
        new_stop.description = request.data["description"]
        new_stop.city = request.data.get("city", None)
        new_stop.country = request.data["country"]
        new_stop.latitude = request.data.get("latitude", 0.0)
        new_stop.longitude = request.data.get("longitude", 0.0)
        new_stop.visited_date = request.data.get("visited_date", None)

        try:
            new_stop.save()
            categories = Category.objects.filter(pk__in=request.data.get("category_ids", []))
            new_stop.categories.set(categories)
            serializer = StopSerializer(Stop.objects.get(pk=new_stop.pk))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
            
    def retrieve(self, request, pk=None):
        """Handle GET requests for single stop

        Returns:
            Response -- JSON serialized instance
        """
        try:
            stop = Stop.objects.get(pk=pk, trip__user=request.auth.user)
            serializer = StopSerializer(stop)
            return Response(serializer.data)
        except Stop.DoesNotExist:
            return Response({"reason": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """Handle PATCH requests

        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            stop = Stop.objects.get(pk=pk, trip__user=request.auth.user)
            if "name" in request.data:
                stop.name = request.data["name"]
            if "description" in request.data:
                stop.description = request.data["description"]
            if "city" in request.data:
                stop.city = request.data["city"]
            if "country" in request.data:
                stop.country = request.data["country"]
            if "visited_date" in request.data:
                stop.visited_date = request.data["visited_date"]
            if "category_ids" in request.data:
                stop.categories.set(Category.objects.filter(pk__in=request.data["category_ids"]))
            stop.save()
        except Stop.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return HttpResponseServerError(ex)

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single stop

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            stop = Stop.objects.get(pk=pk, trip__user=request.auth.user)
            stop.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        except Stop.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests for all stops

        Returns:
            Response -- JSON serialized array
        """
        try:
            stops = Stop.objects.filter(trip__user=request.auth.user).order_by("-start_date")
            serializer = StopSerializer(stops, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

