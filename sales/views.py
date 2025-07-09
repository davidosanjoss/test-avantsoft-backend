from rest_framework import generics
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated

from .models import Sales
from .serializers import SalesFilterSerializer, SalesSerializer


class Sales_LC_View(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = SalesFilterSerializer

    def get(self, request, *args, **kwargs):
        clients = Sales.objects.all().prefetch_related('sales')
        serializer = ClientCustomSerializer(clients, many=True)
        return Response({
            "data": {
                "clientes": serializer.data
            },
            "meta": {
                "registroTotal": clients.count(),
                "pagina": 1  # ou calculado com paginação real
            },
            "redundante": {
                "status": "ok"
            }
        })


class Sales_RUD_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
