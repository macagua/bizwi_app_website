from __future__ import unicode_literals
from django.db import models
from core.client.models import Clients
from core.store.models import Stores


# Promotion status
class PromotionsStatus(models.Model):
    promotions_status_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'promotions_status'


# Type Promotions
class PromotionsType(models.Model):
    promotion_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'promotions_type'


# Promotions
class Promotions(models.Model):
    promotion_id = models.IntegerField(primary_key=True, null=False)
    description = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    active = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    img_url = models.CharField(max_length=250)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    promotion_type = models.ForeignKey(PromotionsType, on_delete=models.CASCADE)
    promotion_status = models.ForeignKey(PromotionsStatus, on_delete=models.CASCADE)

    class Meta:
        db_table = 'promotions'


# Relationship between Promotions and store
class PromotionsOnStores(models.Model):
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotions, on_delete=models.CASCADE)

    class Meta:
        db_table = 'promotions_on_stores'

