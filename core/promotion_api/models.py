from __future__ import unicode_literals

from django.db import models


class Clients(models.Model):
    client_id = models.UUIDField(primary_key=True, null=False)
    business_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    prefix = models.CharField(max_length=4)

    class Meta:
        db_table = 'clients'


class Promotions(models.Model):
    promotion_id = models.UUIDField(primary_key=True, null=False)
    description = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    active = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    img_url = models.CharField(max_length=250)
    promotion_type_id = models.ForeignKey()
    client_id = models.ForeignKey()
    promotion_status_id = models.ForeignKey()


class PromotionsStatus(models.Model):
    promotion_status_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=150, null=False)


