from rest_framework import serializers
from .models import Client, Validity

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ValiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Validity
        field = '__all__'