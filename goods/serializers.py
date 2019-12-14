from rest_framework import serializers
from goods.models import goods, categorygGoods


class GoodsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = goods
        fields = '__all__'

class GoodsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = categorygGoods
        fields = '__all__'