from rest_framework import serializers
from .models import Auto, Olx


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = "__all__"


class AutoSerializerMin(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ['Proizvodjac', 'Model', 'Godiste', 'Cijena']


class OlxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olx
        fields = "__all__"
