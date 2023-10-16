from rest_framework import serializers
from .models import Cats, CatLifeguard

class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cats
        fields = '__all__'
class CatLifeguardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatLifeguard
        fields = '__all__'