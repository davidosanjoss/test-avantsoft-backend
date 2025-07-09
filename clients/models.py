from django.db import models


class Clients(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
