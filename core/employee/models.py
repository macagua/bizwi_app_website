from __future__ import unicode_literals
from django.db import models
from core.store.models import Stores


class Roles(models.Model):
    rol_id = models.IntegerField(primary_key=True, null=False)
    description = models.CharField(max_length=250)

    class Meta:
        db_table = 'roles'


class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True, null=False)
    language = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = 'employees'


class EmployeesStores(models.Model):
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employees_stores'


class Permissions(models.Model):
    permission_id = models.IntegerField(primary_key=True, null=False)
    description = models.CharField(max_length=250)

    class Meta:
        db_table = 'permissions'


class PermissionsRoles(models.Model):
    permission_role_id = models.IntegerField(primary_key=True, null=False)
    permission = models.ForeignKey(Permissions, on_delete=models.CASCADE)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        db_table = 'permissions_roles'







