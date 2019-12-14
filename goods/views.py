from django.shortcuts import render
from rest_framework import generics
from goods.models import goods
from goods.serializers import GoodsListSerializer

# Create your views here.
class GoodListView(generics.ListAPIView):
    serializer_class = GoodsListSerializer
    queryset = goods.objects.all()