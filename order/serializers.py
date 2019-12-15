from rest_framework import serializers
from order.models import order, deliveryAdress, statusDelivery
from clients.models import Client
from django.contrib.auth.models import User

class ClientFioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['fio']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class DeliveryAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = deliveryAdress
        fields = ['adress']

class StatusDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = statusDelivery
        fields = ['name']


class OrdersListSerializer(serializers.ModelSerializer):
    client = ClientFioSerializer(required=True)
    deliveryAdress = DeliveryAdressSerializer(required=True)
    operator = UserSerializer(required=True)
    statusDelivery = StatusDeliverySerializer(required=True)
    class Meta:
        model = order
        fields = ['id','client', 'operator', 'createOrder', 'statusDelivery', 'deliveryAdress','totalSum']