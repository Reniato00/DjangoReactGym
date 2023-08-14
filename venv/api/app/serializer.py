from rest_framework import serializers
from .models import Client, Validity,ClientValidity,Place,PlaceCategoryPlace,CategoryPlace,Coach,PlaceCoach

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ValiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Validity
        field = '__all__'

class ClientValiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientValidity
        field = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        field = '__all__' 

class PlaceCategoryPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceCategoryPlace
        field = '__all__'

class CategoryPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPlace
        field = '__all__'

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        field = '__all__'

class PlaceCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceCoach
        field = '__all__'