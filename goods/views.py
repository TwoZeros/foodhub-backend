from django.shortcuts import render
from rest_framework import generics
from goods.models import goods, categorygGoods
from goods.serializers import GoodsListSerializer

# Create your views here.
class GoodListView(generics.ListAPIView):
    serializer_class = GoodsListSerializer
    queryset = goods.objects.all()

class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = categorygGoods.objects.all()