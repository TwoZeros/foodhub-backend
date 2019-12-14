from django.shortcuts import render
from rest_framework import generics
from order.models import order
from order.serializers import OrdersListSerializer

# Create your views here.
class OrderListSView(generics.ListAPIView):
    serializer_class = OrdersListSerializer
    queryset = order.objects.all()