import factory
from factory.fuzzy import FuzzyDecimal, FuzzyDate
from datetime import date, timedelta
from clients.models import Clients
from sales.models import Sales


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Clients

    full_name = factory.Faker("name")
    email = factory.LazyAttribute(
        lambda obj: f"{obj.full_name.replace(' ', '.').lower()}@example.com")
    birth_date = factory.Faker("date_of_birth")


class SaleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sales

    client = factory.SubFactory(ClientFactory)
    date = FuzzyDate(date.today() - timedelta(days=30), date.today())
    value = FuzzyDecimal(10.0, 1000.0, precision=2)
