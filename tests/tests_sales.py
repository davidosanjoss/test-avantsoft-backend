import pytest
from datetime import date

from sales.models import Sales

from .setup import api_client, SaleFactory, ClientFactory


@pytest.mark.django_db
def test_list_sales(api_client):
    SaleFactory.create_batch(5)
    response = api_client.get("/api/sales/")
    assert response.status_code == 200
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_create_sale(api_client):
    client = ClientFactory()
    data = {
        "client": client.id,
        "date": str(date.today()),
        "value": 199.99
    }
    response = api_client.post("/api/sales/", data)
    assert response.status_code == 201
    assert Sales.objects.filter(client=client, value=199.99).exists()


@pytest.mark.django_db
def test_update_sale(api_client):
    sale = SaleFactory(value=100)
    data = {
        "client": sale.client.id,
        "date": str(sale.date),
        "value": 500
    }
    response = api_client.put(f"/api/sales/{sale.id}/", data)
    assert response.status_code == 200
    sale.refresh_from_db()
    assert float(sale.value) == 500


@pytest.mark.django_db
def test_patch_sale(api_client):
    sale = SaleFactory(value=100)
    patch_data = {"value": 777.77}
    response = api_client.patch(f"/api/sales/{sale.id}/", patch_data)
    assert response.status_code == 200
    sale.refresh_from_db()
    assert float(sale.value) == 777.77


@pytest.mark.django_db
def test_delete_sale(api_client):
    sale = SaleFactory()
    response = api_client.delete(f"/api/sales/{sale.id}/")
    assert response.status_code == 204
    assert not Sales.objects.filter(id=sale.id).exists()


@pytest.mark.django_db
def test_daily_sales_stats_view(api_client):
    client = ClientFactory()
    SaleFactory.create(client=client, value=150, date=date.today())
    SaleFactory.create(client=client, value=50, date=date.today())
    response = api_client.get("/api/statistics/daily-sales/")
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert response.data[0]["valor"] >= 0
