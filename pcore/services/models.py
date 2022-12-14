# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

import datetime
import pytz
# from __future__ import unicode_literals

from colorful.fields import RGBColorField
import django.utils.timezone
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.postgres.fields import JSONField
from django_countries.fields import CountryField
from django_languages import LanguageField
from django_languages.languages import LANGUAGES
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


# Users Models
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, is_admin, **extra_fields):
        now = datetime.datetime.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=False,
                          is_superuser=is_superuser, is_admin=is_admin,
                          last_login=now, date_joined=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, is_staff=False, is_superuser=False, is_admin=False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, is_staff=True, is_superuser=True, is_admin=True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


# Gender for Custom User model
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class CustomUser(AbstractBaseUser):
    """
    """
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_customer_admin = models.BooleanField(default=False)
    is_employee_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name=_('Date joined'), default=django.utils.timezone.now, editable=False)
    lang = models.CharField(max_length=2, default='es', blank=False, null=False)

    class Meta:
        db_table = 'customs_users'

    objects = UserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Does the user have permissions to view the app `app_label`?
        # Simplest possible answer: Yes, always
        return True

    def is_employee(self):
        return False


    def is_client(self):
        return False

    def is_people(self):
        return False


class AuthTypes(models.Model):
    auth_type_id = models.AutoField(primary_key=True)
    auth_type = models.CharField(max_length=30)
    enabled = models.BooleanField()

    class Meta:
        db_table = 'auth_types'


class BrandStyle(models.Model):
    bstyle_id = models.AutoField(primary_key=True)
    brand = models.ForeignKey('Brands', verbose_name=_('Brand'), on_delete=models.DO_NOTHING)
    logo_url = models.URLField(verbose_name=_('Logo Url'), max_length=512, null=True, blank=True)
    favicon_url = models.URLField(verbose_name=_('Favicon Url'), max_length=512)
    bgcolor = RGBColorField(verbose_name=_('Background color'), max_length=7, default='#ffffff')
    fgcolor = RGBColorField(verbose_name=_('Foreground color'), max_length=7, default='#000000')
    background_img = models.CharField(verbose_name=_('Background image'), max_length=512, blank=True, null=True)
    # background_img = models.ImageField(verbose_name=_('Background image'), null=True)
    font = models.CharField(verbose_name=_('Font'), max_length=70, blank=True, null=True)

    # http://stackoverflow.com/questions/2443752/django-display-image-in-admin-interface
    def image_tag(self):
        return u'<img src="%s" />' % (self.logo_url)

    image_tag.short_description = 'Logo URL'
    image_tag.allow_tags = True

    def favicon_tag(self):
        return u'<img src="%s" />' % (self.favicon_url)

    favicon_tag.short_description = 'Favicon Url'
    favicon_tag.allow_tags = True

    # http://stackoverflow.com/questions/3442881/change-font-color-for-a-field-in-django-admin-interface-if-expression-is-true
    def bgfgcolor_brand(self):
        return '<span style="background-color: %s; color: %s;">The Background & Foreground Colors</span>' % (
            self.bgcolor, self.fgcolor)

    bgfgcolor_brand.short_description = 'Background / Foreground Colors'
    bgfgcolor_brand.allow_tags = True
    # bgcolor_brand.admin_order_field = 'brand'

    def __unicode__(self):
        return "Brand Styles of '%s'" % (self.brand)

    class Meta:
        db_table = 'brand_style'
        verbose_name = 'brand style'
        verbose_name_plural = 'brand styles'


@python_2_unicode_compatible  # only if you need to support Python 2
class BrandTags(models.Model):
    brand = models.OneToOneField('Brands', verbose_name=_('Brand'), on_delete=models.DO_NOTHING, primary_key=True)
    tag = JSONField(verbose_name=_('Tag'))

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
    gtin = models.CharField(verbose_name=_('Global Trade Item Number'), max_length=70, default='')
    email = models.EmailField(verbose_name=_('Email'), max_length=75, blank=True, null=True)
    fb_fanpage = models.URLField(verbose_name=_('Facebook Fan Page'), max_length=512, blank=True, null=True)
    url = models.URLField(verbose_name=_('Website Url'), max_length=512, blank=True, null=True)
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

    class Meta:
        db_table = 'cities'
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.city

    def __unicode__(self):
        return "%s" % self.city_name


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True, default='1')
    # country = models.CharField(max_length=200)
    country = CountryField(blank_label='Select a country', default='ES')

    #    def __unicode__(self):
    #        return self.country

    class Meta:
        db_table = 'countries'
        verbose_name = 'country'
        verbose_name_plural = 'countries'


class Coupons(models.Model):
    coupon_id = models.BigIntegerField(primary_key=True)
    promotion = models.ForeignKey('Promotions', on_delete=models.DO_NOTHING)
    coupon_code = models.CharField(max_length=250)
    wallet_uuid = models.ForeignKey('UserWallets', on_delete=models.DO_NOTHING, db_column='wallet_uuid')
    claim_time = models.DateTimeField()
    coupon_status = models.ForeignKey('CouponsStatus', on_delete=models.DO_NOTHING)
    coupon_type = models.ForeignKey('CouponsTypes', on_delete=models.DO_NOTHING)
    short_description = models.CharField(max_length=20)
    long_description = models.CharField(max_length=70)
    legal_statement = models.CharField(max_length=100)
    redemption_start = models.DateTimeField()
    redemption_end = models.DateTimeField()
    publication_start = models.DateTimeField()
    publication_end = models.DateTimeField()
    expiration_time = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    used = models.BooleanField()

    class Meta:
        db_table = 'coupons'
        verbose_name = 'coupon'
        verbose_name_plural = 'coupons'


class CouponsImpacts(models.Model):
    coupon_impact_id = models.AutoField(primary_key=True)
    coupon = models.ForeignKey('Coupons', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('Users', on_delete=models.DO_NOTHING)
    store = models.ForeignKey('Stores', on_delete=models.DO_NOTHING)
    claim_time = models.DateTimeField()

    class Meta:
        db_table = 'coupons_impacts'
        verbose_name = 'coupon impact'
        verbose_name_plural = 'coupons impacts'


class CouponsStatus(models.Model):
    coupon_status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'coupons_status'
        verbose_name = 'coupon status'
        verbose_name_plural = 'coupons status'


class CouponsTypes(models.Model):
    coupon_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'coupons_types'
        verbose_name = 'coupon type'
        verbose_name_plural = 'coupons types'


class CustomerAuthTypes(models.Model):
    cust_auth_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.DO_NOTHING)
    auth_type = models.ForeignKey('AuthTypes', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'customer_auth_types'
        verbose_name = 'customer auth type'
        verbose_name_plural = 'customer auth types'


class CustomerCategories(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.DO_NOTHING)
    customer = models.ForeignKey('Customers', on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s has a category '%s'" % (self.customer, self.category)

    class Meta:
        db_table = 'customer_categories'
        verbose_name = 'customer category'
        verbose_name_plural = 'customer categories'
        unique_together = (('category', 'customer'),)


class CustomerStyles(models.Model):
    style_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.DO_NOTHING)
    logo_url = models.URLField(verbose_name=_('Logo Url'), max_length=512, null=True, blank=True)
    favicon_url = models.URLField(verbose_name=_('Favicon Url'), max_length=512)
    bgcolor = RGBColorField(verbose_name=_('Background color'), max_length=7, default='#ffffff')
    fgcolor = RGBColorField(verbose_name=_('Foreground color'), max_length=7, default='#000000')
    background_img = models.CharField(verbose_name=_('Background image'), max_length=512, blank=True, null=True)
    font = models.CharField(verbose_name=_('Font'), max_length=100, blank=True, null=True)

    # http://stackoverflow.com/questions/2443752/django-display-image-in-admin-interface
    def image_tag(self):
        return u'<img src="%s" />' % (self.logo_url)

    image_tag.short_description = 'Logo URL'
    image_tag.allow_tags = True

    def favicon_tag(self):
        return u'<img src="%s" />' % (self.favicon_url)

    favicon_tag.short_description = 'Favicon Url'
    favicon_tag.allow_tags = True

    # http://stackoverflow.com/questions/3442881/change-font-color-for-a-field-in-django-admin-interface-if-expression-is-true
    def bgfgcolor_brand(self):
        return '<span style="background-color: %s; color: %s;">The Background & Foreground Colors</span>' % (
            self.bgcolor, self.fgcolor)

    bgfgcolor_brand.short_description = 'Background / Foreground Colors'
    bgfgcolor_brand.allow_tags = True

    def __unicode__(self):
        return "Customer Styles of '%s'" % (self.customer)

    class Meta:
        db_table = 'customer_styles'
        verbose_name = 'customer style'
        verbose_name_plural = 'customer styles'


@python_2_unicode_compatible  # only if you need to support Python 2
class CustomerTags(models.Model):
    customer = models.OneToOneField('Customers', on_delete=models.DO_NOTHING, primary_key=True)
    tag = JSONField(verbose_name=_('Tag'))

    def __str__(self):
        return self.tag

    class Meta:
        db_table = 'customer_tags'
        verbose_name = 'customer tag'
        verbose_name_plural = 'customer tags'


@python_2_unicode_compatible  # only if you need to support Python 2
class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    customer_name = models.CharField(verbose_name=_('Customer name'), max_length=60)
    business_name = models.CharField(verbose_name=_('Business name'), max_length=250)
    code_crm = models.CharField(verbose_name=_('CRM Code'), max_length=6)
    prefix = models.CharField(verbose_name=_('Prefix'), max_length=4)
    description = models.CharField(max_length=250)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    fb_fanpage = models.CharField(verbose_name=_('Facebook Fan Page'), max_length=512, blank=True, null=True)
    fb_merchant_id = models.CharField(verbose_name=_('Facebook Merchant Id'), max_length=100, blank=True, null=True)
    gtin = models.CharField(verbose_name=_('Global Trade Item Number'), max_length=70, default='', blank=True,
                            null=True)
    url = models.URLField(max_length=512, null=True, blank=True)
    twitter_id = models.CharField(verbose_name=_('Twitter account'), max_length=100, blank=True, null=True)
    instagram_id = models.CharField(verbose_name=_('Instagram account'), max_length=100, blank=True, null=True)
    google_id = models.CharField(verbose_name=_('Google account'), max_length=100, blank=True, null=True)
    gplus_id = models.CharField(verbose_name=_('Google++ account'), max_length=512, blank=True, null=True)
    lang = LanguageField(verbose_name=_('Language'), choices=LANGUAGES, max_length=3, default='es')
    locale = models.CharField(max_length=10, null=True, blank=True)
    timezone = models.CharField(verbose_name=_('Timezone'), max_length=255, null=True,
                                choices=[(x, x) for x in pytz.common_timezones], default='Europe/Madrid')
    brand_enabled = models.BooleanField(verbose_name=_('Brand enabled?'), default=False)
    age_range = models.CharField(verbose_name=_('Age range'), max_length=2, default='')
    is_active = models.BooleanField(verbose_name=_('Is active?'), default=False)
    creation_date = models.DateTimeField(verbose_name=_('Creation date'), default=django.utils.timezone.now)
    mod_date = models.DateTimeField(verbose_name=_('Modification date'), blank=True, null=True)

    def __str__(self):
        return self.customer_name

    class Meta:
        db_table = 'customers'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'


@python_2_unicode_compatible  # only if you need to support Python 2
class Departments(models.Model):
    department_id = models.IntegerField(verbose_name=_('Department ID'), primary_key=True, default='1')
    stores = models.ForeignKey('Stores', verbose_name=_('Stores'), default='', blank=False, null=False,
                               on_delete=models.DO_NOTHING)
    department = models.CharField(verbose_name=_('Department'), max_length=250, default='')

    def __str__(self):
        return self.department

    def fullname(self):
        return "%s: %s" % self.department

    class Meta:
        db_table = 'departments'
        verbose_name = 'department'
        verbose_name_plural = 'departments'


class Devices(models.Model):
    device_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey('Vendors', on_delete=models.DO_NOTHING)
    mac = models.CharField(max_length=10, blank=True, null=True)
    blue_mac = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    user_agent = models.CharField(max_length=20, blank=True, null=True)
    os_ver = models.CharField(max_length=10)
    os_family = models.CharField(max_length=10)
    first_seen = models.DateTimeField()
    last_seen = models.DateTimeField()

    class Meta:
        db_table = 'devices'
        verbose_name = 'device'
        verbose_name_plural = 'devices'


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


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    uid = models.CharField(unique=True, max_length=16)
    pwd = models.CharField(max_length=128, blank=True, null=True)
    language = LanguageField(verbose_name=_('Language'), choices=LANGUAGES, max_length=3, blank=False, null=True,
                             default='es')  # default lang client
    is_active = models.BooleanField()
    creation_date = models.DateTimeField()
    mod_date = models.DateTimeField(blank=True, null=True)
    last_access = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'employees'
        verbose_name = 'employee'
        verbose_name_plural = 'employees'


class Events(models.Model):
    event_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=70)
    event_header_url = models.URLField(verbose_name=_('Event Header Url'), max_length=512)
    active = models.BooleanField()
    end_date = models.DateField()
    start_time = models.TimeField()
    start_date = models.DateField()
    end_time = models.TimeField()
    client_id = models.IntegerField()
    url = models.URLField(verbose_name=_('Event Url'), max_length=512)

    class Meta:
        db_table = 'events'
        verbose_name = 'event'
        verbose_name_plural = 'events'


class FilterOnPromotion(models.Model):
    promotion_filter = models.AutoField(primary_key=True)
    filter = models.ForeignKey('PromotionsFilters', on_delete=models.DO_NOTHING)
    promotion = models.ForeignKey('Promotions', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'filter_on_promotion'
        verbose_name = 'filter on promotion'
        verbose_name_plural = 'filters on promotions'


@python_2_unicode_compatible  # only if you need to support Python 2
class LocationTags(models.Model):
    store = models.OneToOneField('Locations', on_delete=models.DO_NOTHING, primary_key=True)
    tags = JSONField(verbose_name=_('Tag'))

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


class MessageToCustomer(models.Model):
    sender = models.ForeignKey(Users)
    receiver = models.ForeignKey(Customers)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, editable=False)
    read = models.BooleanField(default=False)

    class Meta:
        db_table = 'message_to_customer'


class MessageToUser(models.Model):
    sender = models.ForeignKey(Customers)
    receiver = models.ForeignKey(Users)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, editable=False)
    read = models.BooleanField(default=False)

    class Meta:
        db_table = 'message_to_user'

class Pedestrians(models.Model):
    pd_id = models.BigIntegerField(primary_key=True)
    sensor = models.ForeignKey('Sensor', on_delete=models.DO_NOTHING)
    department = models.ForeignKey('Departments', on_delete=models.DO_NOTHING)
    store = models.ForeignKey('Stores', on_delete=models.DO_NOTHING)
    sensor_sid = models.CharField(max_length=64)
    device = models.ForeignKey('Devices', on_delete=models.DO_NOTHING)
    ss = models.DecimalField(max_digits=3, decimal_places=0)
    distance = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    band = models.CharField(max_length=10, blank=True, null=True)
    rate = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'pedestrians'
        verbose_name = 'pedestrian'
        verbose_name_plural = 'pedestrians'


class PromoStyle(models.Model):
    promotion = models.OneToOneField('Promotions', on_delete=models.DO_NOTHING, primary_key=True)
    header_url = models.URLField(verbose_name=_('Header Url'), max_length=512)
    img_url = models.URLField(verbose_name=_('Image Url'), max_length=250)
    logo_url = models.URLField(verbose_name=_('Logo Url'), max_length=512, blank=True, null=True)
    favicon_url = models.URLField(verbose_name=_('Favicon Url'), max_length=512, blank=True, null=True)
    bgcolor = RGBColorField(verbose_name=_('Background color'), max_length=7, default='#ffffff')
    fgcolor = RGBColorField(verbose_name=_('Foreground color'), max_length=7, default='#000000')
    background_img = models.CharField(verbose_name=_('Background image'), max_length=512, blank=True, null=True)
    font = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        db_table = 'promo_style'
        verbose_name = 'Promotion style'
        verbose_name_plural = 'Promotions styles'


class PromotionDuration(models.Model):
    promotion_duration_id = models.AutoField(primary_key=True)
    end_time = models.TimeField()
    start_time = models.TimeField()
    monday = models.BooleanField()
    thursday = models.BooleanField()
    wednesday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    tuesday = models.BooleanField()
    promotion = models.ForeignKey('Promotions', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'promotion_duration'
        verbose_name = 'Promotion duration'
        verbose_name_plural = 'Promotions duration'


class Promotions(models.Model):
    promotion_id = models.IntegerField(primary_key=True)
    client_id = models.IntegerField(verbose_name=_('Client ID'), )
    description = models.CharField(verbose_name=_('Description'), max_length=120)
    short_description = models.CharField(verbose_name=_('Short Description'), max_length=70)
    long_description = models.CharField(verbose_name=_('Long Description'), max_length=750)
    name = models.CharField(verbose_name=_('Name'), max_length=250)
    url = models.URLField(verbose_name=_('Url'), max_length=250, blank=True, null=True)
    active = models.BooleanField(verbose_name=_('Is active?'), )
    start_date = models.DateField(verbose_name=_('Start Date'), )
    end_date = models.DateField(verbose_name=_('End Date'), )
    expiration_time_range = models.DateTimeField(verbose_name=_('Expiration Time Range'), )
    promotion_type = models.ForeignKey('PromotionsTypes', verbose_name=_('Promotion Type'), on_delete=models.DO_NOTHING)
    promotion_status = models.ForeignKey('PromotionsStatus', verbose_name=_('Promotion Statu'), on_delete=models.DO_NOTHING)
    send_email = models.BooleanField(verbose_name=_('Send Email?'), )
    send_msg = models.NullBooleanField(verbose_name=_('Send Message?'), )

    class Meta:
        db_table = 'promotions'
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'


class PromotionsFilters(models.Model):
    filter_id = models.IntegerField(verbose_name=_('Filter ID'), primary_key=True)
    filter_name = models.CharField(verbose_name=_('Filter Name'), max_length=50)
    short_description = models.CharField(verbose_name=_('Short Description'), max_length=70)
    description = models.CharField(verbose_name=_('Description'), max_length=512)
    is_enum = models.BooleanField(verbose_name=_('Is Enum?'), )
    enum_orig = models.CharField(verbose_name=_('Enum orig'), max_length=20)
    callback_obj = models.CharField(verbose_name=_('Callback Obj'), max_length=20)
    enabled = models.BooleanField(verbose_name=_('Is Enabled?'), )

    class Meta:
        db_table = 'promotions_filters'
        verbose_name = 'Promotion filter'
        verbose_name_plural = 'Promotions filters'


class PromotionsForBrands(models.Model):
    brand = models.ForeignKey('Brands', verbose_name=_('Brand'), on_delete=models.DO_NOTHING)
    promotion = models.ForeignKey('Promotions', verbose_name=_('Promotion'), on_delete=models.DO_NOTHING)
    updated_at = models.DateTimeField(verbose_name=_('Updated at'), )
    store = models.ForeignKey('Stores', verbose_name=_('Store'), on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'promotions_for_brands'
        verbose_name = 'Promotion for brand'
        verbose_name_plural = 'Promotions for brands'
        unique_together = (('brand', 'promotion'),)


class PromotionsLoyalty(models.Model):
    promotion = models.OneToOneField('Promotions', verbose_name=_('Promotion'), on_delete=models.DO_NOTHING, primary_key=True)
    num_checkins = models.IntegerField(verbose_name=_('Number Checkins'), )

    class Meta:
        db_table = 'promotions_loyalty'
        verbose_name = 'Promotion loyalty'
        verbose_name_plural = 'Promotions loyalties'


class PromotionsOnStores(models.Model):
    store = models.ForeignKey('Stores', verbose_name=_('Store'), on_delete=models.DO_NOTHING)
    promotion = models.ForeignKey('Promotions', verbose_name=_('Promotion'), on_delete=models.DO_NOTHING)
    updated_at = models.DateTimeField(verbose_name=_('Updated at'), )

    class Meta:
        db_table = 'promotions_on_stores'
        verbose_name = 'Promotion on store'
        verbose_name_plural = 'Promotions on stores'
        unique_together = (('store', 'promotion'),)


class PromotionsStatus(models.Model):
    promotion_status_id = models.AutoField(verbose_name=_('Promotion Status ID'), primary_key=True)
    name = models.CharField(verbose_name=_('Name'), max_length=150)

    class Meta:
        db_table = 'promotions_status'
        verbose_name = 'Promotion status'
        verbose_name_plural = 'Promotions status'


class PromotionsTypes(models.Model):
    promotion_type_id = models.AutoField(verbose_name=_('Promotion Type ID'), primary_key=True)
    name = models.CharField(verbose_name=_('Name'), max_length=250)

    class Meta:
        db_table = 'promotions_types'


@python_2_unicode_compatible  # only if you need to support Python 2
class Sensor(models.Model):
    sensor_id = models.AutoField(primary_key=True, default='1')
    department = models.ForeignKey('Departments', verbose_name=_('Department'), null=True, on_delete=models.DO_NOTHING)
    sid = models.CharField(verbose_name=_('Sensor SID'), max_length=120, unique=True)
    name = models.CharField(verbose_name=_('Name'), max_length=100, blank=True, null=True)
    model = models.ForeignKey('SensorModels', verbose_name=_('Model'), on_delete=models.DO_NOTHING)
    mac = models.CharField(verbose_name=_('MAC Address'), max_length=17, unique=True)
    sensor_ip = models.GenericIPAddressField(verbose_name=_('Sensor IP'), protocol='IPv4', null=True)
    call_home = models.BooleanField(verbose_name=_('Call home?'), default=False)
    rate = models.FloatField(verbose_name=_('Rate'), blank=True, null=True)
    public_key = models.CharField(verbose_name=_('Public Key'), max_length=700)
    essid = models.CharField(verbose_name=_('ESSID'), max_length=200, blank=True, null=True)
    register_time = models.DateTimeField(verbose_name=_('Register time'), null=True, default=django.utils.timezone.now)
    last_access = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.mac

    class Meta:
        db_table = 'sensor'
        verbose_name = 'sensor'
        verbose_name_plural = 'sensors'


class SensorLocation(models.Model):
    sensor = models.OneToOneField('Sensor', verbose_name=_('Sensor'), on_delete=models.DO_NOTHING, primary_key=True)
    latitude = models.DecimalField(verbose_name=_('Latitude'), max_digits=7, decimal_places=5)
    longitude = models.DecimalField(verbose_name=_('Longitude'), max_digits=8, decimal_places=5)
    point = models.TextField(verbose_name=_('Point'), blank=True, null=True)
    geoloc_poly = models.TextField(verbose_name=_('Model'), blank=True, null=True)
    distance_threshold = models.DecimalField(verbose_name=_('Distance Threshold'), max_digits=5, decimal_places=2)
    accuracy = models.IntegerField(verbose_name=_('Accuracy'), )

    class Meta:
        db_table = 'sensor_location'
        verbose_name = 'Sensor location'
        verbose_name_plural = 'Sensor locations'


class SensorModels(models.Model):
    model_id = models.AutoField(verbose_name=_('Model ID'), primary_key=True)
    model = models.CharField(verbose_name=_('Model'), max_length=20)
    description = models.CharField(verbose_name=_('Description'), max_length=70, blank=True, null=True)
    is_mobile = models.BooleanField(verbose_name=_('Is Mobile?'), )

    class Meta:
        db_table = 'sensor_models'
        verbose_name = 'sensor model'
        verbose_name_plural = 'sensors models'


class StoreStyle(models.Model):
    sstyle_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('Stores', verbose_name=_('Store'), on_delete=models.CASCADE)
    logo_url = models.URLField(verbose_name=_('Logo Url'), max_length=512, blank=True, null=True)
    favicon_url = models.URLField(verbose_name=_('Favicon Url'), max_length=512, blank=True, null=True)
    bgcolor = RGBColorField(verbose_name=_('Background color'), max_length=7, default='#ffffff')
    fgcolor = RGBColorField(verbose_name=_('Foreground color'), max_length=7, default='#000000')
    background_img = models.CharField(verbose_name=_('Background image'), max_length=512, blank=True, null=True)
    font = models.CharField(verbose_name=_('Font'), max_length=70, blank=True, null=True)

    # http://stackoverflow.com/questions/2443752/django-display-image-in-admin-interface
    def image_tag(self):
        return u'<img src="%s" />' % (self.logo_url)

    image_tag.short_description = 'Logo URL'
    image_tag.allow_tags = True

    def favicon_tag(self):
        return u'<img src="%s" />' % (self.favicon_url)

    favicon_tag.short_description = 'Favicon Url'
    favicon_tag.allow_tags = True

    # http://stackoverflow.com/questions/3442881/change-font-color-for-a-field-in-django-admin-interface-if-expression-is-true
    def bgfgcolor_brand(self):
        return '<span style="background-color: %s; color: %s;">The Background & Foreground Colors</span>' % (
            self.bgcolor, self.fgcolor)

    bgfgcolor_brand.short_description = 'Background / Foreground Colors'
    bgfgcolor_brand.allow_tags = True

    def __unicode__(self):
        return "Store Styles of '%s'" % (self.store)

    class Meta:
        db_table = 'store_style'
        verbose_name = 'store style'
        verbose_name_plural = 'store styles'


class Stores(models.Model):
    store_id = models.AutoField(primary_key=True, default='1')
    customer = models.ForeignKey('Customers', default='', blank=False, null=False)
    store_name = models.CharField(verbose_name=_('Store name'), max_length=100, null=True)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    url = models.URLField(verbose_name=_('Website Url'), max_length=400, null=True, blank=True)
    address = models.CharField(verbose_name=_('Address'), max_length=512, null=True)
    phone = models.CharField(verbose_name=_('Phone'), max_length=20, null=True)
    timezone = models.CharField(verbose_name=_('Timezone'), max_length=255, null=True,
                                choices=[(x, x) for x in pytz.common_timezones], default='Europe/Madrid')
    lang = LanguageField(verbose_name=_('Language'), choices=LANGUAGES, max_length=3, default='es')
    is_active = models.BooleanField(verbose_name=_('Is active?'), default=False)
    creation_date = models.DateTimeField(verbose_name=_('Creation date'), default=django.utils.timezone.now)
    last_access = models.DateTimeField(verbose_name=_('Last date'), blank=True, null=True)
    mod_date = models.DateTimeField(verbose_name=_('Modification date'), blank=True, null=True)

    def fullname(self):
        return "%s: %s" % self.store_name

    def __unicode__(self):
        return self.store_name

    class Meta:
        db_table = 'stores'
        verbose_name = 'store'
        verbose_name_plural = 'stores'


class UserIdentities(models.Model):
    user_identity_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', verbose_name=_('User'), on_delete=models.DO_NOTHING)
    email = models.CharField(verbose_name=_('Email'), max_length=75, blank=True, null=True)
    phone = models.CharField(verbose_name=_('Phone'), max_length=20, blank=True, null=True)
    gravatar = models.CharField(verbose_name=_('Gravatar'), max_length=512)
    access_token = models.CharField(verbose_name=_('Access Token'), max_length=100, blank=True, null=True)
    auth_social_id = models.CharField(verbose_name=_('Auth Social ID'), max_length=10)
    device = models.ForeignKey('Devices', verbose_name=_('Device'), on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'user_identities'
        verbose_name = 'user identity'
        verbose_name_plural = 'user identities'


class UserProfile(models.Model):
    user = models.OneToOneField('Users', verbose_name=_('User'), on_delete=models.DO_NOTHING, primary_key=True)
    relationship_status = models.CharField(max_length=60, blank=True, null=True)
    screen_name = models.CharField(verbose_name=_('Screen Name'), max_length=60)
    interests = models.BinaryField()
    profile_image_url = models.URLField(verbose_name=_('Profile Image Url'), max_length=512, blank=True, null=True)
    gravatar = models.CharField(verbose_name=_('Gravatar'), max_length=512)
    bio = models.CharField(verbose_name=_('Biography'), max_length=512, blank=True, null=True)
    friends_count = models.IntegerField(verbose_name=_('Friends count'))
    username = models.CharField(verbose_name=_('Username'), max_length=20, blank=True, null=True)
    twitter_id = models.CharField(verbose_name=_('Twitter account'), max_length=20, blank=True, null=True)
    facebook_link = models.URLField(verbose_name=_('Facebook URL'), max_length=512, null=True, blank=True, default=None)
    facebook_id = models.BigIntegerField(verbose_name=_('Facebook ID'), null=True, blank=True, default=0)
    gplus_id = models.BigIntegerField(verbose_name=_('Google++ account'), blank=True, null=True)
    gplus_link = models.URLField(verbose_name=_('Google++ URL'), max_length=512, null=True, blank=True)
    google_id = models.CharField(verbose_name=_('Google account'), max_length=75, blank=True, null=True)

    class Meta:
        db_table = 'user_profile'
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'


class UserWallets(models.Model):
    wallet_uuid = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('Users', verbose_name=_('User'), on_delete=models.DO_NOTHING)
    enabled = models.BooleanField(verbose_name=_('Is Enabled?'), )

    class Meta:
        db_table = 'user_wallets'
        verbose_name = 'user wallet'
        verbose_name_plural = 'user wallets'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=20)
    name = models.CharField(verbose_name=_('Name'), max_length=30)
    lastname = models.CharField(verbose_name=_('Last Name'), max_length=30)
    firstname = models.CharField(verbose_name=_('First Name'), max_length=30)
    city = models.ForeignKey('Cities', verbose_name=_('City'), on_delete=models.DO_NOTHING)
    country = models.ForeignKey('Countries', verbose_name=_('Country'), on_delete=models.DO_NOTHING)
    timezone = models.IntegerField(verbose_name=_('Timezone'), )
    gender = models.CharField(verbose_name=_('Gender'), max_length=1, blank=True, null=True)
    birthdate = models.DateField(verbose_name=_('Birthdate'), blank=True, null=True)
    locale = models.CharField(verbose_name=_('Locale'), max_length=8)
    language = LanguageField(verbose_name=_('Language'), choices=LANGUAGES, max_length=3, blank=False, null=True, default='es')
    date_joined = models.DateTimeField(verbose_name=_('Date Joined'), )
    last_access = models.DateTimeField(verbose_name=_('Last Access'), blank=True, null=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Vendors(models.Model):
    vendor_id = models.CharField(verbose_name=_('Vendor ID'), primary_key=True, max_length=10)
    name = models.CharField(verbose_name=_('Name'), max_length=30)

    class Meta:
        db_table = 'vendors'
        verbose_name = 'vendor'
        verbose_name_plural = 'vendors'

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
