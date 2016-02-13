from __future__ import unicode_literals
from django.db import models
from core.promotion.models import Promotions
from core.store.models import Stores
from core.user.models import Users


class CouponsStatus(models.Model):
    coupon_status_id = models.IntegerField(primary_key=True, null=False)
    description = models.CharField(max_length=250)

    class Meta:
        db_table = 'coupons_status'


class CouponsType(models.Model):
    coupon_type_id = models.IntegerField(primary_key=True, null=False)
    description = models.CharField(max_length=250)

    class Meta:
        db_table = 'coupons_type'


class Coupons(models.Model):
    coupon_id = models.UUIDField(primary_key=True, null=False)
    promotion = models.ForeignKey(Promotions, on_delete=models.CASCADE)
    claim_time = models.DateTimeField(auto_now_add=True)
    coupon_status = models.ForeignKey(CouponsStatus, on_delete=models.CASCADE)
    coupon_type = models.ForeignKey(CouponsType, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=500)
    log_description = models.TextField()
    legal_statement = models.TextField()
    redemption_start = models.DateTimeField()
    redemption_end = models.DateTimeField()
    publication_start = models.DateTimeField()
    publication_end = models.DateTimeField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        db_table = 'coupons'


class CouponsUsers(models.Model):
    coupon = models.ForeignKey(Coupons, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'coupons_users'


class CouponsImpacts(models.Model):
    coupon_impact_id = models.IntegerField(primary_key=True, null=False)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        db_table = 'coupons_impacts'





