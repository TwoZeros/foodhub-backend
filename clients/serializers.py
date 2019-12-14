from rest_framework import serializers
from clients.models import Client


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['fio', 'telephone', 'status_client']