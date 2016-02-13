from __future__ import unicode_literals

from django.db import models
from core.device.models import Devices


class AuthSocial(models.Model):
    auth_social_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=250)
    client_secret = models.CharField(max_length=250)
    client_id = models.CharField(max_length=250)
    uri = models.CharField(max_length=500)

    class Meta:
        db_table = 'auth_social'


class Users(models.Model):
    user_id = models.UUIDField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    gender = models.CharField(max_length=3)
    birthday = models.DateField()
    city = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=500)
    timezone = models.CharField(max_length=10)
    language = models.CharField(max_length=10)
    locale = models.CharField(max_length=10)
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'users'


class UsersIdentity(models.Model):
    user_identity = models.IntegerField(primary_key=True, null=False)
    gravatar_url = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    auth_social = models.ForeignKey(AuthSocial, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users_identity'


class UsersProfile(models.Model):
    user_profile_id = models.IntegerField(primary_key=True, null=False)
    username = models.CharField(max_length=100)
    screen_name = models.CharField(max_length=100)
    language = models.CharField(max_length=10)
    bio = models.TextField()
    status = models.BooleanField()
    friends_count = models.IntegerField()
    relationship_status = models.CharField(max_length=120)
    skills = models.TextField()
    occupation = models.CharField(max_length=200)
    interest = models.CharField(max_length=200)
    profile_image_url = models.CharField(max_length=500)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users_profile'

