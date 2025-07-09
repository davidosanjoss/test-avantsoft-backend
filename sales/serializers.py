from rest_framework import serializers
from django_filters import rest_framework as filters

from .models import Sales


class SalesFilterSerializer(filters.FilterSet):
    class Meta:
        model = Sales
        fields = {
            "client": ["exact"],
            "date": ["exact", "gte", "lte"],
            "value": ["exact", "gte", "lte"],
        }


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"


class SalesRelatedSerializer(serializers.Serializer):
    data = serializers.DateField(source='date')
    valor = serializers.DecimalField(max_digits=10, decimal_places=2, source='value')
