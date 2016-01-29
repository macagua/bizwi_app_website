from __future__ import unicode_literals
from django.db import models
from core.store.models import Departaments


class Sensors(models.Model):
    sensor_id = models.IntegerField(primary_key=True, null=False)
    sid = models.CharField(max_length=120)
    model = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    mac = models.CharField(max_length=17)
    call_home = models.BooleanField()
    rate = models.DecimalField()
    public_key = models.TextField()
    essid = models.CharField(max_length=200)
    register_time = models.DateTimeField()
    sensor_ip = models.CharField(max_length=100)
    departament = models.ForeignKey(Departaments, on_delete=models.CASCADE())

    class Meta:
        db_table = 'sensors'
