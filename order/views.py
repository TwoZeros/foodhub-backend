from django.shortcuts import render
from rest_framework import generics
from order.models import order, goodsByOrder
from order.serializers import OrdersListSerializer, GoodsByOrderSerializer

# Create your views here.
class OrderListSView(generics.ListAPIView):
    serializer_class = OrdersListSerializer
    queryset = order.objects.all()


class GoodsByOrderView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoodsByOrderSerializer
    queryset = goodsByOrder.objects.all()