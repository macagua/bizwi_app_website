# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-03 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthSocial',
            fields=[
                ('auth_social_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('client_secret', models.CharField(max_length=250)),
                ('client_id', models.CharField(max_length=250)),
                ('uri', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'auth_social',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=3)),
                ('birthday', models.DateField()),
                ('city', models.CharField(max_length=100)),
                ('photo_url', models.CharField(max_length=500)),
                ('timezone', models.CharField(max_length=10)),
                ('language', models.CharField(max_length=10)),
                ('locale', models.CharField(max_length=10)),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UsersIdentity',
            fields=[
                ('user_identity', models.IntegerField(primary_key=True, serialize=False)),
                ('gravatar_url', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=100)),
                ('access_token', models.CharField(max_length=100)),
                ('auth_social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.AuthSocial')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Devices')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Users')),
            ],
            options={
                'db_table': 'users_identity',
            },
        ),
        migrations.CreateModel(
            name='UsersProfile',
            fields=[
                ('user_profile_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('screen_name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=10)),
                ('bio', models.TextField()),
                ('status', models.BooleanField()),
                ('friends_count', models.IntegerField()),
                ('relationship_status', models.CharField(max_length=120)),
                ('skills', models.TextField()),
                ('occupation', models.CharField(max_length=200)),
                ('interest', models.CharField(max_length=200)),
                ('profile_image_url', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Users')),
            ],
            options={
                'db_table': 'users_profile',
            },
        ),
    ]
