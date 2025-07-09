from rest_framework import generics
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated

from .models import Clients
from .paginations import CustomPagination
from .serializers import ClientsFilterSerializer, ClientsSerializer, ClientCustomSerializer


class Clients_LC_View(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = ClientsFilterSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        clients = Clients.objects.all().prefetch_related('sales')

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(clients, request)
        serializer = ClientCustomSerializer(page, many=True)

        return Response({
            "data": {
                "clientes": serializer.data
            },
            "meta": {
                "registroTotal": paginator.page.paginator.count,
                "pagina": paginator.page.number
            },
            "redundante": {
                "status": "ok"
            }
        })


class Clients_RUD_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
