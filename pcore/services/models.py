# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# import datetime
import pytz
# from __future__ import unicode_literals

import django.utils.timezone
from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.postgres.fields import JSONField
from django_countries.fields import CountryField
from django_languages import LanguageField
from django_languages.languages import LANGUAGES
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible  # only if you need to support Python 2
class BrandStyle(models.Model):
    bstyle_id = models.AutoField(primary_key=True)
    brand = models.ForeignKey('Brands', verbose_name=_('Brand'), on_delete=models.DO_NOTHING)
    logo_url = models.URLField(verbose_name=_('Logo Url'), max_length=512, null=True, blank=True)
    favicon_url = models.URLField(verbose_name=_('Favicon Url'), max_length=512)
    bgcolor = models.CharField(verbose_name=_('Background color'), max_length=7)
    fgcolor = models.CharField(verbose_name=_('Foreground color'), max_length=7)
    background_img = models.CharField(verbose_name=_('Background image'), max_length=512, blank=True, null=True)
    font = models.CharField(verbose_name=_('Font'), max_length=70, blank=True, null=True)

    class Meta:
        db_table = 'brand_style'
        verbose_name = 'brand style'
        verbose_name_plural = 'brand styles'


@python_2_unicode_compatible  # only if you need to support Python 2
class BrandTags(models.Model):
    brand = models.OneToOneField('Brands', verbose_name=_('Brand'), on_delete=models.DO_NOTHING, primary_key=True)
    tag = JSONField()

    def __str__(self):
        return self.tag

    class Meta:
        db_table = 'brand_tags'
        verbose_name = 'brand tag'
        verbose_name_plural = 'brand tags'


@python_2_unicode_compatible  # only if you need to support Python 2
class Brands(models.Model):
    brand_id = models.AutoField(primary_key=True, default='1')
    customer = models.ForeignKey('Customers', default='', blank=False, null=False, on_delete=models.DO_NOTHING)
    brand_name = models.CharField(verbose_name=_('Brand name'), max_length=100)
    description = models.CharField(verbose_name=_('Description'), max_length=512, blank=True, null=True)
    gtin = models.CharField(max_length=70, default='')
    email = models.EmailField(verbose_name=_('Email'), max_length=75, blank=True, null=True)
    fb_fanpage = models.URLField(verbose_name=_('Facebook Fan Page'), max_length=512, blank=True, null=True)
    url = models.URLField(max_length=512, blank=True, null=True)
    google_id = models.CharField(verbose_name=_('Google account'), max_length=100, blank=True, null=True)
    fb_merchant_id = models.CharField(verbose_name=_('Facebook Merchant Id'), max_length=100, blank=True, null=True)
    instagram_id = models.CharField(verbose_name=_('Instagram account'), max_length=100, blank=True, null=True)
    twitter_id = models.CharField(verbose_name=_('Twitter account'), max_length=100, blank=True, null=True)
    gplus_id = models.CharField(verbose_name=_('Google++ account'), max_length=512, blank=True, null=True)
    age_range = models.CharField(verbose_name=_('Age range'), max_length=2, default='')
    is_active = models.BooleanField(verbose_name=_('Is active?'), default=False)
    creation_date = models.DateTimeField(verbose_name=_('Creation date'), default=django.utils.timezone.now)
    last_access = models.DateTimeField(verbose_name=_('Last date'), blank=True, null=True)
    mod_date = models.DateTimeField(verbose_name=_('Modification date'), blank=True, null=True)

    def __str__(self):
        return self.brand_name

    def fullname(self):
        return "%s: %s" % self.brand_name

    class Meta:
        db_table = 'brands'
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


@python_2_unicode_compatible  # only if you need to support Python 2
class Categories(models.Model):
    category_id = models.AutoField(primary_key=True, default='1')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return "%s" % self.categories_name


@python_2_unicode_compatible  # only if you need to support Python 2
class Cities(models.Model):
    city_id = models.AutoField(primary_key=True, default='1')
    city = models.CharField(verbose_name=_('City'), max_length=100, default='')
    country = models.ForeignKey('Countries', verbose_name=_('Country'), on_delete=models.CASCADE)

    def __str__(self):
        return self.city

    class Meta:
        db_table = 'cities'
        verbose_name = 'city'
        verbose_name_plural = 'cities'
    
    def __unicode__(self):
        return "%s" % self.city_name


@python_2_unicode_compatible  # only if you need to support Python 2
class Countries(models.Model):
    country_id = models.AutoField(primary_key=True, default='1')
    # country = models.CharField(max_length=200)
    country = CountryField(blank_label='Select a country')

    def __str__(self):
        return self.country

    class Meta:
        db_table = 'countries'
        verbose_name = 'country'
        verbose_name_plural = 'countries'
        
    def __unicode__(self):
        return "%s" % self.country_name


class CustomerCategories(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.DO_NOTHING)
    customer = models.ForeignKey('Customers', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'customer_categories'
        verbose_name = 'customer category'
        verbose_name_plural = 'customer categories'
        unique_together = (('category', 'customer'),)


@python_2_unicode_compatible  # only if you need to support Python 2
class CustomerStyles(models.Model):
    style_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.DO_NOTHING)
    logo_url = models.URLField(verbose_name=_('Logo Url'), max_length=512, null=True, blank=True)
    favicon_url = models.URLField(verbose_name=_('Logo Url'), max_length=512)
    bgcolor = models.CharField(verbose_name=_('Background color'), max_length=7, default='#ffffff')
    fgcolor = models.CharField(verbose_name=_('Foreground color'), max_length=7, default='#ffffff')
    background_img = models.CharField(verbose_name=_('Background image'), max_length=512, blank=True, null=True)
    font = models.CharField(verbose_name=_('Font'), max_length=100, blank=True, null=True)

    def __str__(self):
        return self.style_id

    class Meta:
        db_table = 'customer_styles'
        verbose_name = 'customer style'
        verbose_name_plural = 'customer styles'


@python_2_unicode_compatible  # only if you need to support Python 2
class CustomerTags(models.Model):
    customer = models.OneToOneField('Customers', on_delete=models.DO_NOTHING, primary_key=True)
    tag = JSONField()

    def __str__(self):
        return self.tag

    class Meta:
        db_table = 'customer_tags'
        verbose_name = 'customer tag'
        verbose_name_plural = 'customer tags'


@python_2_unicode_compatible  # only if you need to support Python 2
class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(verbose_name=_('Customer name'), max_length=60)
    business_name = models.CharField(verbose_name=_('Business name'), max_length=250)
    code_crm = models.CharField(verbose_name=_('Code CRM'), max_length=6)
    prefix = models.CharField(verbose_name=_('Prefix'), max_length=4)
    description = models.CharField(max_length=250)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    fb_fanpage = models.CharField(verbose_name=_('Facebook Fan Page'), max_length=512, blank=True, null=True)
    fb_merchant_id = models.CharField(verbose_name=_('Facebook Merchant Id'), max_length=100, blank=True, null=True)
    gtin = models.CharField(verbose_name=_('Gtin'), max_length=70, default='', blank=True, null=True)
    url = models.URLField(max_length=512, null=True, blank=True)
    twitter_id = models.CharField(verbose_name=_('Twitter account'), max_length=100, blank=True, null=True)
    instagram_id = models.CharField(verbose_name=_('Instagram account'), max_length=100, blank=True, null=True)
    google_id = models.CharField(verbose_name=_('Google account'), max_length=100, blank=True, null=True)
    gplus_id = models.CharField(verbose_name=_('Google++ account'), max_length=512, blank=True, null=True)
    lang = LanguageField(verbose_name=_('Language'), choices=LANGUAGES, max_length=3, default='es')
    locale = models.CharField(max_length=10, null=True, blank=True)
    timezone = models.CharField(verbose_name=_('Timezone'), max_length=255, null=True, choices=[(x, x) for x in pytz.common_timezones], default='Europe/Madrid')
    brand_enabled = models.BooleanField(verbose_name=_('Brand enabled?'), default=False)
    age_range = models.CharField(verbose_name=_('Age range'), max_length=2, default='')
    is_active = models.BooleanField(verbose_name=_('Is active?'), default=False)
    creation_date = models.DateTimeField(verbose_name=_('Creation date'), default=django.utils.timezone.now)
    last_access = models.DateTimeField(verbose_name=_('Last date'), blank=True, null=True)
    mod_date = models.DateTimeField(verbose_name=_('Modification date'), blank=True, null=True)

    def __str__(self):
        return self.customer_name

    class Meta:
        db_table = 'customers'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'


@python_2_unicode_compatible  # only if you need to support Python 2
class Departments(models.Model):
    department_id = models.IntegerField(primary_key=True, default='1')
    stores = models.ForeignKey('Stores', verbose_name=_('Stores'), default='', blank=False, null=False, on_delete=models.DO_NOTHING)
    department = models.CharField(verbose_name=_('Department'), max_length=250, default='')

    def __str__(self):
        return "%s: %s" % self.department_name

    def fullname(self):
        return "%s: %s" % self.department_name

    class Meta:
        db_table = 'departments'
        verbose_name = 'department'
        verbose_name_plural = 'departments'


@python_2_unicode_compatible  # only if you need to support Python 2
class Districts(models.Model):
    district_id = models.AutoField(primary_key=True)
    country = models.ForeignKey('Countries', verbose_name=_('Country'), on_delete=models.CASCADE)
    district = models.CharField(verbose_name=_('District'), max_length=80)
    localname = models.CharField(verbose_name=_('Local name'), max_length=80)

    def __str__(self):
        return self.district

    class Meta:
        db_table = 'districts'
        verbose_name = 'district'
        verbose_name_plural = 'districts'


@python_2_unicode_compatible  # only if you need to support Python 2
class LocationTags(models.Model):
    store = models.OneToOneField('Locations', on_delete=models.DO_NOTHING, primary_key=True)
    tags = JSONField()

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'location_tags'
        verbose_name = 'location tag'
        verbose_name_plural = 'location tags'


class Locations(models.Model):
    store = models.OneToOneField('Stores', on_delete=models.DO_NOTHING, primary_key=True)
    latitude = models.DecimalField(verbose_name=_('Latitude'), max_digits=7, decimal_places=5)
    longitude = models.DecimalField(verbose_name=_('Longitude'), max_digits=8, decimal_places=5)
    point = models.TextField(verbose_name=_('Point'), blank=True, null=True)
    geoloc_poly = models.TextField(verbose_name=_('Geoloc poly'), blank=True, null=True)
    distance_threshold = models.DecimalField(verbose_name=_('Distance threshold'), max_digits=5, decimal_places=2)
    city = models.ForeignKey('Cities', verbose_name=_('City'), on_delete=models.DO_NOTHING)
    district = models.ForeignKey('Districts', verbose_name=_('District'), on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'locations'
        verbose_name = 'location'
        verbose_name_plural = 'locations'

# Sensor Models
MODELS = (
    ('Model 01', 'MR-01'),
    ('Model 02', 'MR-02'),
    ('Model 03', 'MR-03'),
    ('Model 04', 'MR-04'),
    ('Model 05', 'MR-05'),
)


@python_2_unicode_compatible  # only if you need to support Python 2
class Sensor(models.Model):
    sensor_id = models.AutoField(primary_key=True, default='1')
    department = models.ForeignKey('Departments', verbose_name=_('Department'), null=True, on_delete=models.DO_NOTHING)
    sid = models.CharField(verbose_name=_('SID'), max_length=120, unique=True)
    model = models.CharField(verbose_name=_('Model'), max_length=30, choices=MODELS, null=True)
    name = models.CharField(verbose_name=_('Name'), max_length=100, blank=True, null=True)
    mac = models.CharField(verbose_name=_('MAC Address'), max_length=17, unique=True)
    call_home = models.BooleanField(verbose_name=_('Call home?'), default=False)
    rate = models.FloatField(verbose_name=_('Rate'), blank=True, null=True)
    public_key = models.CharField(verbose_name=_('Public Key'), max_length=700)
    essid = models.CharField(verbose_name=_('ESSID'), max_length=200, blank=True, null=True)
    register_time = models.DateTimeField(verbose_name=_('Register time'), null=True, default=django.utils.timezone.now)
    sensor_ip = models.GenericIPAddressField(verbose_name=_('Sensor IP'), protocol='IPv4', null=True)

    def __str__(self):
        return "%s" % self.mac

    class Meta:
        db_table = 'sensor'
        verbose_name = 'sensor'
        verbose_name_plural = 'sensors'


@python_2_unicode_compatible  # only if you need to support Python 2
class StoreStyle(models.Model):
    sstyle_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('Stores', on_delete=models.CASCADE)
    logo_url = models.URLField(verbose_name=_('Logo Url'), max_length=512, blank=True, null=True)
    favicon_url = models.URLField(verbose_name=_('Favicon Url'), max_length=512, blank=True, null=True)
    bgcolor = models.CharField(verbose_name=_('Background color'), max_length=7)
    fgcolor = models.CharField(verbose_name=_('Foreground color'), max_length=7)
    background_img = models.CharField(verbose_name=_('Background image'), max_length=512, blank=True, null=True)
    font = models.CharField(verbose_name=_('Font'), max_length=70, blank=True, null=True)

    def __str__(self):
        return self.sstyle_id

    class Meta:
        # managed = False
        db_table = 'store_style'
        verbose_name = 'store style'
        verbose_name_plural = 'store styles'


@python_2_unicode_compatible  # only if you need to support Python 2
class Stores(models.Model):
    store_id = models.AutoField(primary_key=True, default='1')
    customer = models.ForeignKey('Customers', default='', blank=False, null=False)
    store_name = models.CharField(verbose_name=_('Store name'), max_length=100, null=True)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    url = models.URLField(verbose_name=_('Url'), max_length=400, null=True, blank=True)
    address = models.CharField(verbose_name=_('Address'), max_length=512, null=True)
    phone = models.CharField(verbose_name=_('Phone'), max_length=20, null=True)
    timezone = models.CharField(verbose_name=_('Timezone'), max_length=255, choices=[(x, x) for x in pytz.common_timezones], null=True)
    lang = LanguageField(verbose_name=_('Language'), choices=LANGUAGES, max_length=3, default='es')
    is_active = models.BooleanField(verbose_name=_('Is active?'), default=False)
    creation_date = models.DateTimeField(verbose_name=_('Creation date'), default=django.utils.timezone.now)
    last_access = models.DateTimeField(verbose_name=_('Last date'), blank=True, null=True)
    mod_date = models.DateTimeField(verbose_name=_('Modification date'), blank=True, null=True)
    
    def __str__(self):
        return "%s: %s" % self.store_name

    def fullname(self):
        return "%s: %s" % self.store_name

    class Meta:
        # managed = False
        db_table = 'stores'
        verbose_name = 'store'
        verbose_name_plural = 'stores'


# Users Models
# class UserManager(BaseUserManager):
#     def _create_user(self, username, email, password, is_staff, is_superuser, is_admin, **extra_fields):
#         now = datetime.datetime.now()
#         if not username:
#             raise ValueError(_('The given username must be set'))
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email,
#                           is_staff=is_staff, is_active=False,
#                           is_superuser=is_superuser, is_admin=is_admin,
#                           last_login=now, date_joined=now,
#                           **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, username, email=None, password=None, **extra_fields):
#         return self._create_user(username, email, password, is_staff=False, is_superuser=False, is_admin=False,
#                                  **extra_fields)

#     def create_superuser(self, username, email, password, **extra_fields):
#         user = self._create_user(username, email, password, is_staff=True, is_superuser=True, is_admin=True,
#                                  **extra_fields)
#         user.is_active = True
#         user.save(using=self._db)
#         return user


# Status for Promotions model
# STATUS_CHOICES = (
#     ('P', 'Pending'),
#     ('A', 'Accepted'),
#     ('D', 'Denied'),
# )

# Gender for Custom User model
# GENDER_CHOICES = (
#     ('M', 'Male'),
#     ('F', 'Female'),
# )


# class CustomUser(AbstractBaseUser):
#     """
#     """
#     username = models.CharField(max_length=30, unique=True, blank=True, null=True)
#     email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
#     first_name = models.CharField(max_length=100, blank=False, null=False)
#     last_name = models.CharField(max_length=100, blank=False, null=False)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
#     birthday = models.DateField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     is_client_admin = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=datetime.datetime.now(), editable=False)
#     lang = models.CharField(max_length=2, default='es', blank=False, null=False)

#     class Meta:
#         db_table = 'customs_users'

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     def get_full_name(self):
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         return self.first_name

#     def has_perm(self, perm, obj=None):
#         # Does the user have a specific permission?
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         # Does the user have permissions to view the app `app_label`?
#         # Simplest possible answer: Yes, always
#         return True

#     def is_employee(self):
#         return False

#     def is_client(self):
#         return False

#     def is_people(self):
#         return False


# class Regions(models.Model):
#     region_id = models.AutoField(primary_key=True, default='1')
#     region_name = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'regions'

#     def __unicode__(self):
#         return "%s" % self.region_name


# class business logic
# class Clients(CustomUser):
#     client_name = models.CharField(max_length=100, null=True, blank=True)
#     code_crm = models.CharField(max_length=10, null=True, blank=True)
#     telephone = models.CharField(max_length=50, null=True)
#     web_site = models.URLField(null=True, blank=True)
#     description = models.CharField(max_length=250, null=True)
#     logo_url = models.URLField(null=True, blank=True)
#     background_color = models.CharField(max_length=7, default='#ffffff')
#     foreground_color = models.CharField(max_length=7, default='#ffffff')
#     background_img = models.URLField(null=True, blank=True)
#     ttf_font = models.CharField(max_length=100, null=True, blank=True)
#     promotion_enable = models.BooleanField(default=False)
#     city = models.ForeignKey(Cities, null=True, on_delete=models.CASCADE)
#     country = models.ForeignKey(Countries, null=True, on_delete=models.CASCADE)
#     photo_url = models.URLField(null=True, blank=True)
#     facebook_id = models.BigIntegerField(null=True, blank=True, default=0)
#     facebook_link = models.URLField(null=True, blank=True, default=None)
#     facebook_fan_page = models.URLField(null=True, blank=True)
#     facebook_merchant_id = models.CharField(max_length=250, null=True)
#     twitter_account = models.CharField(max_length=250, null=True)
#     gplus_id = models.CharField(max_length=30, null=True, blank=True, default=None)
#     language = models.CharField(max_length=10, null=True, blank=True)
#     locale = models.CharField(max_length=10, null=True, blank=True)
#     timezone = models.CharField(max_length=255, choices=[(x, x) for x in pytz.common_timezones], null=True)

#     class Meta:
#         db_table = 'clients'

#     def is_client(self):
#         return True


# class Employees(CustomUser):
#     language = models.CharField(max_length=2, blank=False, null=True) # default lang client
#     is_store_manager = models.BooleanField(default=False)
#     is_marketing = models.BooleanField(default=False)
#     phone_employee = models.CharField(max_length=20, blank=True, null=True)
#     confirmation_code = models.CharField(max_length=66, blank=True, null=True)
#     token = models.CharField(max_length=200, blank=True, null=True)
#     client = models.ForeignKey(Clients, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'employees'

#     def is_employee(self):
#         return True


# class Tags(models.Model):
#     tag = models.AutoField(primary_key=True, default='1')
#     tag_name = models.CharField(max_length=255)
#     store = models.ManyToManyField(Stores)

#     class Meta:
#         db_table = 'tags'

#     def __unicode__(self):
#         return "%s" % self.tag_name


# class PromotionsTypes(models.Model):
#     promotion_type_id = models.AutoField(primary_key=True, default='1')
#     promotion_type_name = models.CharField(max_length=50, default='default')
#     description = models.CharField(max_length=100)

#     def __str__(self):
#         return "%s: %s" % self.promotion_type_name

#     def fullname(self):
#         return "%s: %s" % self.promotion_type_name

#     class Meta:
#         db_table = 'promotions_types'


# class PromotionsFilters(models.Model):
#     promotion_filter_id = models.AutoField(primary_key=True, default='1')
#     promotion_filter_name = models.CharField(max_length=50)
#     description = models.CharField(max_length=100)

#     def __str__(self):
#         return "%s: %s" % self.promotion_filter_name

#     def fullname(self):
#         return "%s: %s" % (self.promotion_filter_name)

#     class Meta:
#         db_table = 'promotions_filters'


# class PromotionsLoyalties(models.Model):
#     promotion_loyalty_id = models.AutoField(primary_key=True, default='1')
#     promotion_loyalty_name = models.CharField(max_length=50)
#     check_in_number = models.DecimalField(max_digits=3, decimal_places=0, default=0)
#     description = models.CharField(max_length=100)

#     def __str__(self):
#         return "%s: %s" % (self.promotion_loyalty_name)

#     def fullname(self):
#         return "%s: %s" % (self.promotion_loyalty_name)

#     class Meta:
#         db_table = 'promotions_loyalties'


# class PromotionsSpecials(models.Model):
#     promotion_special_id = models.AutoField(primary_key=True, default='1')
#     promotion_special_name = models.CharField(max_length=50)
#     description = models.CharField(max_length=100)
#     def __str__(self):
#         return "%s: %s" % (self.promotion_special_name)

#     def fullname(self):
#         return "%s: %s" % (self.promotion_special_name)

#     class Meta:
#         db_table = 'promotions_specials'



# class Promotions(models.Model):
#     promotion_id = models.AutoField(primary_key=True, default='1')
#     client = models.ForeignKey(Clients, blank=False, null=False)
#     promotion_name = models.CharField(max_length=100)
#     register_date = models.DateTimeField(default=datetime.datetime.now())
#     description = models.TextField()
#     short_description  = models.CharField(max_length=100)
#     long_description = models.TextField()
#     url = models.URLField(max_length=200, null=True, blank=True)
#     status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
#     active = models.BooleanField(default=True)
#     start_date = models.DateField(null=True, blank=True)
#     end_date = models.DateField(null=True, blank=True)
#     start_time = models.TimeField(null=True, blank=True)
#     end_time = models.TimeField(null=True, blank=True)
#     monday = models.BooleanField(default=True)
#     tuesday = models.BooleanField(default=True)
#     wednesday = models.BooleanField(default=True)
#     thursday = models.BooleanField(default=True)
#     friday = models.BooleanField(default=True)
#     saturday = models.BooleanField(default=True)
#     sunday = models.BooleanField(default=True)
#     img_url = models.URLField(max_length=200, null=True, blank=True)
#     email_send = models.BooleanField(default=True)
#     expiration_time_range = models.DateTimeField(default=datetime.datetime.now())
#     promotion_type = models.ForeignKey(PromotionsTypes, null=True)
#     promotion_filter = models.ManyToManyField(PromotionsFilters)

#     def __unicode__(self):
#         return "%s" % self.promotion_name

#     class Meta:
#         db_table = 'promotions'


# class PromotionsImpacts(models.Model):
#     promotion = models.ForeignKey(Promotions)
#     client = models.ForeignKey(Clients)
#     store = models.ForeignKey(Stores, on_delete=models.CASCADE)
#     impact_time = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())
#     promo_code = models.CharField(max_length=200, null=True, blank=True)
#     check_in = models.BooleanField(default=False)
#     check_in_number = models.DecimalField(max_digits=3, decimal_places=0, default=0)
#     check_in_time = models.DateTimeField(null=True, blank=True)

#     class Meta:
#         db_table = 'promotions_impacts'
