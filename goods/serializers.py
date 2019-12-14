from rest_framework import serializers
from goods.models import goods


class GoodsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = goods
        fields = '__all__'