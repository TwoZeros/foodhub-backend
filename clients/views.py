from django.shortcuts import render
from rest_framework import generics
from clients.models import Client, Status_client
from clients.serializers import ClientListSerializer, AllStatusClientSerializer, CreateClientSerializer

# Create your views here.
class ClientListView(generics.ListAPIView):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()


class AllStatusListView(generics.ListAPIView):
    serializer_class = AllStatusClientSerializer
    queryset = Status_client.objects.values('id', 'name')

class ClientCreateView(generics.CreateAPIView):
    serializer_class = CreateClientSerializer