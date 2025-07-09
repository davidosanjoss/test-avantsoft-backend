from django.db import models

from clients.models import Clients


class Sales(models.Model):
    client = models.ForeignKey(Clients, related_name='sales', on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
