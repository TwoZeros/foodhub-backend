from rest_framework import serializers
from clients.models import Client, Status_client

class AllStatusClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status_client
        fields = ['id', 'name']

class StatusClientSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Status_client
        fields = ['name']

class ClientListSerializer(serializers.ModelSerializer):
    status_client = StatusClientSerizalizer(required=True)
    class Meta:
        model = Client
        fields = ['id','fio', 'email', 'telephone', 'status_client']

class CreateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'