from rest_framework import serializers
# from .models import CustomUser, Countries, Cities, Regions, Employees, Customers, Stores, Tags, Categories, Departments, Sensor, Brands, PromotionsTypes, PromotionsFilters, PromotionsLoyalties, PromotionsSpecials, Promotions, PromotionsImpacts
from .models import Countries, Cities, Customers, \
    Stores, Categories, Departments, Sensor, Brands, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'birthday',
                  'lang',
                  'gender',
                  'last_login')


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields =  ('country_id',
                   'country')


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields =  ('city_id',
                   'city',
                   'country')


# class RegionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Regions
#         fields =  ('region_id',
#                    'region_name')


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('customer_name',
                  'business_name',
                  'code_crm',
                  'prefix',
                  'description',
                  'telephone',
                  'email',
                  'gtin',
                  'url',
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
                  'fb_fanpage',
                  'fb_merchant_id',
                  'twitter_id',
                  'instagram_id',
                  'google_id',
                  'gplus_id',
                  'lang',
                  'locale',
                  'timezone',
                  'brand_enabled',
                  'age_range',
                  'is_active',
                  'creation_date',
                  'last_access',
                  'mod_date')


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employees
#         fields = ('id',
#                   'username',
#                   'first_name',
#                   'last_name',
#                   'email',
#                   'is_client_admin',
#                   'is_store_manager',
#                   'is_marketing',
#                   'is_active',
#                   'is_superuser',
#                   'client')


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = ('store_id',
                  'store_name',
                   'register_date',
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
                   'promotion_enable')


# class TagsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tags
#         fields = ('tag',
#                   'tag_name',
#                   'store')


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


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
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


# class PromotionsTypesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PromotionsTypes
#         fields = ('promotion_type_id',
#                   'promotion_type_name',
#                   'description')


# class PromotionsFiltersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PromotionsFilters
#         fields =  ('promotion_filter_id',
#                    'promotion_filter_name',
#                    'description')


# class PromotionsLoyaltiesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PromotionsLoyalties
#         fields =  ('promotion_loyalty_id',
#                    'promotion_loyalty_name',
#                    'check_in_number',
#                    'description')


# class PromotionsSpecialsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PromotionsSpecials
#         fields =  ('promotion_special_id',
#                    'promotion_special_name',
#                    'description')


# class PromotionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Promotions
#         fields =  ('promotion_id',
#                    'client',
#                    'promotion_name',
#                    'register_date',
#                    'description',
#                    'short_description',
#                    'long_description',
#                    'url',
#                    'status',
#                    'active',
#                    'start_date',
#                    'end_date',
#                    'start_time',
#                    'end_time',
#                    'monday',
#                    'tuesday',
#                    'wednesday',
#                    'thursday',
#                    'friday',
#                    'saturday',
#                    'sunday',
#                    'img_url',
#                    'email_send',
#                    'expiration_time_range',
#                    'promotion_type',
#                    'promotion_filter')


# class PromotionsImpactsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PromotionsImpacts
#         fields =  ('promotion',
#                    'client',
#                    'store ',
#                    'impact_time',
#                    'promo_code',
#                    'check_in',
#                    'check_in_number',
#                    'check_in_time')
