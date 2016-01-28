from __future__ import unicode_literals

from django.db import models


# Brands
class Brands(models.Model):
    brand_id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    url = models.CharField(max_length=200)
    timezone = models.CharField(max_length=255)
    cover_img_url = models.CharField(max_length=200)
    lowercolor = models.CharField(max_length=7)
    uppercolor = models.CharField(max_length=7)

    class Meta:
        db_table = 'brands'

