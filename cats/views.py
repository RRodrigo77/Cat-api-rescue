from rest_framework import viewsets
from rest_framework.response import Response
from cats.models import Cats, CatLifeguard
from cats.serializers import CatsSerializer, CatLifeguardSerializer

class CatsViewSet(viewsets.ModelViewSet):
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer

class CatLifeguardViewSet(viewsets.ModelViewSet):
    queryset = CatLifeguard.objects.all()
    serializer_class = CatLifeguardSerializer