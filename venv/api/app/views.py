from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ClientSerializer,ValiditySerializer
from .models import Client,Validity
# Create your views here.

class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all() 

class ValidtyView(viewsets.ModelViewSet):
    serializer_class = ValiditySerializer
    queryset=  Validity.objects.all()
