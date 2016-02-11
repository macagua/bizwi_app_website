from rest_framework import serializers
from .models import Employees, Clients, Stores, Tags, Brands, Departments, Promotions, PromotionsTypes


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


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('client_id',
                  'client_name',
                  'code_crm',
                  'telephone',
                  'web_site',
                  'description',
                  'logo_url',
                  'background_color',
                  'foreground_color',
                  'background_img',
                  'ttf_font',
                  'promotion_enable',
                  'city',
                  'country',
                  'photo_url',
                  'facebook_id',
                  'facebook_link',
                  'facebook_fanpage',
                  'facebook_merchant_id',
                  'twitter_account',
                  'gplus_id',
                  'language',
                  'locale',
                  'timezone')