from rest_framework import serializers
from .models import Countries, Cities, Regions, Employees, Clients, Stores, Tags, Categories, Departments, Sensors, Brands, PromotionsTypes, PromotionsFilters, PromotionsLoyalties, PromotionsSpecials, Promotions, PromotionsImpacts

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields =  ('country_id',
                   'country_name')


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields =  ('city_id',
                   'city_name',
                   'country')


class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields =  ('region_id',
                   'region_name')


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('client_name',
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
                  'facebook_fan_page',
                  'facebook_merchant_id',
                  'twitter_account',
                  'gplus_id',
                  'language',
                  'locale',
                  'timezone')


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


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = ('store_id',
                   'client',
                   'store_name',
                   'register_date',
                   'region',
                   'country',
                   'city',
                   'address',
                   'geoloc_point',
                   'distance_threshold',
                   'geoloc_poly',
                   'telephone',
                   'web_site',
                   'description',
                   'logo_url',
                   'background_color',
                   'foreground_color',
                   'background_img',
                   'ttf_font',
                   'is_active',
                   'promotion_enable',
                   'employee')


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('tag',
                  'tag_name',
                  'store')


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('category',
                  'categories_name',
                  'store')


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('department_id',
                  'store',
                  'department_name',
                  'register_date',
                  'geoloc_point',
                  'distance_threshold',
                  'geoloc_poly')


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = ('sensor_id',
                  'sid',
                  'model',
                  'name',
                  'mac ',
                  'call_home',
                  'rate',
                  'public_key',
                  'essid',
                  'register_time',
                  'sensor_ip',
                  'department')


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields =  ('brand_id',
                   'client',
                   'brand_name',
                   'register_date',
                   'telephone',
                   'web_site',
                   'description',
                   'logo_url',
                   'background_color',
                   'foreground_color',
                   'background_img',
                   'ttf_font',
                   'is_active',
                   'promotion_enable')


class PromotionsTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionsTypes
        fields = ('promotion_type_id',
                  'promotion_type_name',
                  'description')


class PromotionsFiltersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionsFilters
        fields =  ('promotion_filter_id',
                   'promotion_filter_name',
                   'description')


class PromotionsLoyaltiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionsLoyalties
        fields =  ('promotion_loyalty_id',
                   'promotion_loyalty_name',
                   'check_in_number',
                   'description')

class PromotionsSpecialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionsSpecials
        fields =  ('promotion_special_id',
                   'promotion_special_name',
                   'description')


class PromotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotions
        fields =  ('promotion_id',
                   'client',
                   'promotion_name',
                   'register_date',
                   'description',
                   'short_description',
                   'long_description',
                   'url',
                   'status',
                   'active',
                   'start_date',
                   'end_date',
                   'start_time',
                   'end_time',
                   'monday',
                   'tuesday',
                   'wednesday',
                   'thursday',
                   'friday',
                   'saturday',
                   'sunday',
                   'img_url',
                   'email_send',
                   'expiration_time_range',
                   'promotion_type',
                   'promotion_filter')


class PromotionsImpactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionsImpacts
        fields =  ('promotion',
                   'client',
                   'store ',
                   'impact_time',
                   'promo_code',
                   'check_in',
                   'check_in_number',
                   'check_in_time')