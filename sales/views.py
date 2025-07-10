from django.db.models import Sum
from django.db.models.functions import TruncDate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Sales
from .serializers import SalesFilterSerializer, SalesSerializer


class Sales_LC_View(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = SalesFilterSerializer


class Sales_RUD_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class DailySalesStatsView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = (
            Sales.objects
            .annotate(date_only=TruncDate('date'))
            .values('date_only')
            .annotate(total=Sum('value'))
            .order_by('date_only')
        )
        return Response([
            {"data": d["date_only"], "valor": d["total"]} for d in data
        ])
