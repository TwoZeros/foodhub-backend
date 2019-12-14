from django.shortcuts import render
from rest_framework import generics
from clients.models import Client
from clients.serializers import ClientListSerializer

# Create your views here.
class ClientListView(generics.ListAPIView):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()