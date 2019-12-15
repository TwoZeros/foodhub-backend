from rest_framework import serializers
from goods.models import goods, categorygGoods

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = categorygGoods
        fields = '__all__'


class GoodsListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(required=True)
    class Meta:
        model = goods
        fields = '__all__'

