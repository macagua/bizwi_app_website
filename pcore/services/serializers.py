from rest_framework import serializers
from .models import Employees


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'is_client_admin',
                  'is_store_manager',
                  'is_marketing',
                  'is_active',
                  'is_superuser')
