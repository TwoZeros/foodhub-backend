from rest_framework import serializers
from order.models import order, deliveryAdress
from clients.models import Client

class ClientFioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['fio']


class DeliveryAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = deliveryAdress
        fields = ['client']


class OrdersListSerializer(serializers.ModelSerializer):
    client = ClientFioSerializer(required=True)
    deliveryAdress = DeliveryAdressSerializer(required=True)
    class Meta:
        model = order
        fields = ['client', 'operator', 'createOrder', 'statusDelivery', 'deliveryAdress']