from __future__ import unicode_literals

from django.db import models


class Clients(models.Model):
    client_id = models.UUIDField()
    business_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    prefix = models.CharField(max_length=4)

    class Meta:
        pass


