from rest_framework import serializers
from django_filters import rest_framework as filters

from .models import Clients
from sales.serializers import SalesRelatedSerializer


class ClientsFilterSerializer(filters.FilterSet):
    class Meta:
        model = Clients
        fields = {
            "id": ["exact"],
            "full_name": ["exact", "contains"],
            "email": ["exact", "contains"],
            "birth_date": ["exact"],
        }


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"

        read_only_fields = ("id",)


class DetailsSerializer(serializers.Serializer):
    email = serializers.EmailField()
    nascimento = serializers.DateField(source='birth_date')


class InfoSerializer(serializers.Serializer):
    nomeCompleto = serializers.CharField(source='full_name')
    detalhes = DetailsSerializer(source='*')


class ClientCustomSerializer(serializers.Serializer):
    info = InfoSerializer(source='*')
    estatisticas = serializers.SerializerMethodField()
    duplicado = serializers.SerializerMethodField()

    def get_estatisticas(self, obj):
        vendas = obj.sales.all()
        return {
            "vendas": SalesRelatedSerializer(vendas, many=True).data
        }

    def get_duplicado(self, obj):
        return {
            "nomeCompleto": obj.full_name
        }
