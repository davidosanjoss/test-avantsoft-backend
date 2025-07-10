import pytest
from datetime import date, timedelta

from clients.models import Clients

from .setup import api_client, ClientFactory, SaleFactory


@pytest.mark.django_db
def test_list_clients(api_client):
    ClientFactory.create_batch(3)
    response = api_client.get("/api/clients/")
    assert response.status_code == 200
    assert "clientes" in response.data["data"]
    assert len(response.data["data"]["clientes"]) > 0


@pytest.mark.django_db
def test_retrieve_client(api_client):
    client_obj = ClientFactory()
    response = api_client.get(f"/api/clients/{client_obj.id}/")
    assert response.status_code == 200
    assert response.data["id"] == client_obj.id


@pytest.mark.django_db
def test_create_client(api_client):
    data = {
        "full_name": "João Silva",
        "email": "joao@example.com",
        "birth_date": "1990-01-01"
    }
    response = api_client.post("/api/clients/", data)
    assert response.status_code == 201
    assert Clients.objects.filter(email="joao@example.com").exists()


@pytest.mark.django_db
def test_update_client(api_client):
    client_obj = ClientFactory(full_name="Original Name")
    data = {
        "full_name": "Updated Name",
        "email": client_obj.email,
        "birth_date": str(client_obj.birth_date)
    }
    response = api_client.put(f"/api/clients/{client_obj.id}/", data)
    assert response.status_code == 200
    client_obj.refresh_from_db()
    assert client_obj.full_name == "Updated Name"


@pytest.mark.django_db
def test_patch_client(api_client):
    client_obj = ClientFactory(full_name="Nome Original")
    patch_data = {"full_name": "Nome Atualizado"}
    response = api_client.patch(f"/api/clients/{client_obj.id}/", patch_data)
    assert response.status_code == 200
    client_obj.refresh_from_db()
    assert client_obj.full_name == "Nome Atualizado"


@pytest.mark.django_db
def test_delete_client(api_client):
    client_obj = ClientFactory()
    response = api_client.delete(f"/api/clients/{client_obj.id}/")
    assert response.status_code == 204
    assert not Clients.objects.filter(id=client_obj.id).exists()


@pytest.mark.django_db
def test_top_customers_stats_view(api_client):
    client1 = ClientFactory()
    client2 = ClientFactory()
    SaleFactory.create_batch(3, client=client1, value=100, date=date.today())
    SaleFactory.create_batch(2, client=client2, value=300, date=date.today() - timedelta(days=1))
    response = api_client.get("/api/statistics/top-customers/")
    assert response.status_code == 200
    assert "maior_volume" in response.data
    assert "maior_media" in response.data
    assert "maior_frequencia" in response.data
