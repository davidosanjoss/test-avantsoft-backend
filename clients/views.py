from django.db.models import Sum, Avg, Count
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
        clients = Clients.objects.all().prefetch_related('sales').order_by('full_name')

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


class TopCustomersStatsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = {}

        top_total = (
            Clients.objects
            .annotate(total=Sum('sales__value'))
            .order_by('-total')
            .first()
        )
        data["maior_volume"] = {
            "id": top_total.id,
            "nome": top_total.full_name,
            "total_vendido": top_total.sales.aggregate(total=Sum('value'))['total']
        } if top_total else {}

        top_avg = (
            Clients.objects
            .annotate(avg=Avg('sales__value'))
            .order_by('-avg')
            .first()
        )
        data["top_avg"] = {
            "id": top_avg.id,
            "nome": top_avg.full_name,
            "media_valor": top_avg.sales.aggregate(avg=Avg('value'))['avg']
        } if top_total else {}

        top_freq = (
            Clients.objects
            .annotate(freq=Count('sales__date', distinct=True))
            .order_by('-freq')
            .first()
        )
        data["top_freq"] = {
            "id": top_freq.id,
            "nome": top_freq.full_name,
            "dias_com_venda": top_freq.sales.values('date').distinct().count()
        } if top_total else {}

        return Response(data, status=200)
