from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ClientSerializer,ValiditySerializer, ClientValiditySerializer,PlaceSerializer,CoachSerializer,CategoryPlaceSerializer,PlaceCategoryPlaceSerializer,PlaceCoachSerializer
from .models import Client,Validity,ClientValidity,Place,PlaceCategoryPlace,CategoryPlace,Coach,PlaceCoach
# Create your views here.

class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all() 

class ValidtyView(viewsets.ModelViewSet):
    serializer_class = ValiditySerializer
    queryset=  Validity.objects.all()

class ClientValidityView(viewsets.ModelViewSet):
    serializer_class = ClientValiditySerializer
    queryset = ClientValidity.objects.all()

class PlaceView(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

class PlaceCategoryPlaceView(viewsets.ModelViewSet):
    serializer_class = PlaceCategoryPlaceSerializer
    queryset = PlaceCategoryPlace.objects.all()

class CategoryPlaceView(viewsets.ModelViewSet):
    serializer_class = CategoryPlaceSerializer
    queryset = CategoryPlace.objects.all()

class CoachView(viewsets.ModelViewSet):
    serializer_class = CoachSerializer
    queryset = Coach.objects.all()

class PlaceCoachView(viewsets.ModelViewSet):
    serializer_class = PlaceCoachSerializer
    queryset = PlaceCoach.objects.all()