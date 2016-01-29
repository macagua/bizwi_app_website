from __future__ import unicode_literals

from django.db import models


class Cities(models.Model):
    city_id = models.IntegerField(primary_key=True, null=False)
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE())

    class Meta:
        db_table = 'cities'


class Countries(models.Model):
    country_id = models.IntegerField(primary_key=True, null=False)
    country = models.CharField(max_length=200)

    class Meta:
        db_table = 'countries'


class Departments(models.Model):
    department_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=250)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE())

    class Meta:
        db_table = 'departments'


class Locations(models.Model):
    location_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=150)
    address = models.CharField(200)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    distance_threshold = models.DecimalField(max_digits=5, decimal_places=2)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE())
    store = models.ForeignKey(Stores, on_delete=models.CASCADE())
    
    class Meta:
        db_table = 'locations'


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

