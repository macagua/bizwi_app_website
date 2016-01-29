from __future__ import unicode_literals
from django.db import models


# Devices 
class Devices(models.Model):
    device_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=200)
    mac = models.CharField(max_length=17)
    type = models.CharField(max_length=250)
    family = models.CharField(max_length=30)
    os_family = models.CharField(max_length=30)
    os_version = models.CharField(max_length=100)
    first_seen = models.DateTimeField()
    last_seen = models.DateTimeField()
    user_agent = models.TextField()
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE())

    class Meta:
        db_table = 'devices'


class Vendors(models.Model):
    oui = models.CharField(max_length=17)
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'vendor'








