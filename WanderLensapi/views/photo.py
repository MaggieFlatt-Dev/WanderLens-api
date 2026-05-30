
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from WanderLensapi.models.photo import Photo
from WanderLensapi.models.stop import Stop
from WanderLensapi.serializers.photo import PhotoSerializer


class PhotoView(ViewSet):
    """Photo view set"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized instance
        """
        try:
            stop = Stop.objects.get(pk=request.data["stop_id"], trip__user=request.auth.user)
            photo = Photo()
            photo.stop = stop
            photo.image = request.FILES["image"]
            photo.description = request.data.get("description", "")
            photo.save()
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Stop.DoesNotExist:
            return Response({"reason": "Stop not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized instance
        """
        try:
            photo = Photo.objects.get(pk=pk, stop__trip__user=request.auth.user)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        except Photo.DoesNotExist:
            return Response({"reason": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single item

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            photo = Photo.objects.get(pk=pk, stop__trip__user=request.auth.user)
            photo.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Photo.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests for all items

        Returns:
            Response -- JSON serialized array
        """
        try:
            photos = Photo.objects.filter(stop__trip__user=request.auth.user)
            stop_id = request.query_params.get("stop_id", None)
            if stop_id:
                photos = photos.filter(stop__id=stop_id)
            serializer = PhotoSerializer(photos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
