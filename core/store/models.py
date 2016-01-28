from __future__ import unicode_literals

from django.db import models


# Models
class Stores(models.Model):
    store_id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=400)
    timezone = models.CharField(max_length=255)
    img_url = models.CharField(max_length=200)
    cover_img_url = models.CharField(max_length=400)

    class Meta:
        db_table = 'stores'
