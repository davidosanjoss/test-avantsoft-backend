import pytest
from tests.setup.factories import ClientFactory, SaleFactory


@pytest.fixture
def client_factory():
    return ClientFactory


@pytest.fixture
def sale_factory():
    return SaleFactory
