from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Clients(models.Model):
    client_id = models.UUIDField(primary_key=True, null=False)
    business_name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=250)
    prefix = models.CharField(max_length=4)
    description = models.CharField(max_length=250)
    telephone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)

    class Meta:
        db_table = 'clients'

