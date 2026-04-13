from rest_framework import generics, permissions

from api.serializers import ServiceSerializer, StudioClassSerializer
from services.models import Service
from studio_classes.models import StudioClass


# Create your views here.
class ServiceListViewApi(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]

class StudioClassListViewApi(generics.ListAPIView):
    queryset = StudioClass.objects.all()
    serializer_class = StudioClassSerializer
    permission_classes = [permissions.AllowAny]