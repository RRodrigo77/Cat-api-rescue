from rest_framework import viewsets
from rest_framework.response import Response
from cats.models import Cats
from cats.serializers import CatsSerializer

class CatsViewSet(viewsets.ModelViewSet):
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer