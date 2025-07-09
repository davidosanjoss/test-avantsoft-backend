from rest_framework import generics
from rest_framework.views import Response, Request, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Clients
from .serializers import ClientsFilterSerializer, ClientsResponseSerializer, ClientCustomSerializer


class Clients_LC_View(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsResponseSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = ClientsFilterSerializer

    def get(self, request, *args, **kwargs):
        clients = Clients.objects.all().prefetch_related('sales')
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


class Clients_RUD_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsResponseSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
