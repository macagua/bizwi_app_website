from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import pytz
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


STATUS_CHOICES = (
    ('P', 'Pending'),
    ('A', 'Accepted'),
    ('D', 'Denied'),
)

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
    is_client_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.datetime.now(), editable=False)
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


# class basic
class Countries(models.Model):
    country_id = models.AutoField(primary_key=True,default='1')
    country_name = models.CharField(max_length=200, default='default')

    class Meta:
        db_table = 'countries'
        
    def __unicode__(self):
        return "%s" % self.country_name


class Cities(models.Model):
    city_id = models.AutoField(primary_key=True,default='1')
    city_name = models.CharField(max_length=100)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cities'
    
    def __unicode__(self):
        return "%s" % self.city_name


class Regions(models.Model):
    region_id = models.AutoField(primary_key=True,default='1')
    region_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'regions'
        
    def __unicode__(self):
        return "%s" % self.region_name


# class business logic
class Clients(CustomUser):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    code_crm = models.CharField(max_length=10, null=True, blank=False)
    telephone = models.CharField(max_length=50, null=True)
    web_site = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=250, null=True)
    logo_url = models.URLField(null=True, blank=True)
    background_color = models.CharField(max_length=7, default='#ffffff')
    foreground_color = models.CharField(max_length=7, default='#ffffff')
    background_img = models.URLField(null=True, blank=True)
    ttf_font = models.CharField(max_length=100, null=True, blank=True)
    promotion_enable = models.BooleanField(default=False)
    city = models.ForeignKey(Cities, null=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, null=True, on_delete=models.CASCADE)
    photo_url = models.URLField(null=True, blank=True)
    facebook_id = models.BigIntegerField(null=True, blank=True, default=0)
    facebook_link = models.URLField(null=True, blank=True, default=None)
    facebook_fan_page = models.URLField(null=True, blank=True)
    facebook_merchant_id = models.CharField(max_length=250, null=True)
    twitter_account = models.CharField(max_length=250, null=True)
    gplus_id = models.CharField(max_length=30, null=True, blank=True, default=None)
    language = models.CharField(max_length=10, null=True, blank=True)
    locale = models.CharField(max_length=10, null=True, blank=True)
    timezone = models.CharField(max_length=255, choices=[(x, x) for x in pytz.common_timezones], null=True)

    class Meta:
        db_table = 'clients'

    def is_client(self):
        return True


class Employees(CustomUser):
    language = models.CharField(max_length=2, blank=False, null=True) # default lang client
    is_store_manager = models.BooleanField(default=False)
    is_marketing = models.BooleanField(default=False)
    phone_employee = models.CharField(max_length=20, blank=True, null=True)
    confirmation_code = models.CharField(max_length=66, blank=True, null=True)
    token = models.CharField(max_length=200, blank=True, null=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employees'

    def is_employee(self):
        return True


class Stores(models.Model):
    store_id = models.AutoField(primary_key=True, default='1')
    client = models.ForeignKey(Clients, blank=False, null=False)
    store_name = models.CharField(max_length=100, null=True)
    register_date = models.DateTimeField(default=datetime.datetime.now())
    region = models.ForeignKey(Regions, blank=True, null=True)
    country = models.ForeignKey(Countries, blank=True, null=True)
    city = models.ForeignKey(Cities, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    geoloc_point = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    distance_threshold = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    geoloc_poly = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=50, null=True)
    web_site = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=250, null=True)
    logo_url = models.URLField(null=True, blank=True)
    background_color = models.CharField(max_length=7, default='#ffffff')
    foreground_color = models.CharField(max_length=7, default='#ffffff')
    background_img = models.ImageField(upload_to='media')
    ttf_font = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    promotion_enable = models.BooleanField(default=False)
    employee = models.ManyToManyField(Employees)
    
    def __str__(self):
        return "%s: %s" % self.store_name

    def fullname(self):
        return "%s: %s" % self.store_name

    class Meta:
        db_table = 'stores'
        

class Tags(models.Model):
    tag = models.AutoField(primary_key=True,default='1')
    tag_name = models.CharField(max_length=255)
    store = models.ManyToManyField(Stores)

    class Meta:
        db_table = 'tags'

    def __unicode__(self):
        return "%s" % self.tag_name


class Categories(models.Model):
    category = models.AutoField(primary_key=True,default='1')
    categories_name = models.CharField(max_length=255)
    store = models.ManyToManyField(Stores)
    
    class Meta:
        db_table = 'categories'

    def __unicode__(self):
        return "%s" % self.categories_name


class Departments(models.Model):
    department_id = models.AutoField(primary_key=True,default='1')
    store = models.ForeignKey(Stores, blank=False, null=False)
    department_name = models.CharField(max_length=100,default='all')
    register_date = models.DateTimeField(default=datetime.datetime.now())
    geoloc_point = models.DecimalField(decimal_places=2, max_digits=5)
    distance_threshold = models.DecimalField(decimal_places=2, max_digits=5)
    geoloc_poly = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "%s: %s" % self.department_name

    def fullname(self):
        return "%s: %s" % self.department_name

    class Meta:
        db_table = 'departments'

MODELS = (
    ('Model 01', 'MR-01'),
    ('Model 02', 'MR-02'),
    ('Model 03', 'MR-03'),
    ('Model 04', 'MR-04'),
    ('Model 05', 'MR-05'),
)


class Sensors(models.Model):
    sensor_id = models.AutoField(primary_key=True,default='1')
    sid = models.CharField(max_length=120, unique=True)
    model = models.CharField(max_length=30, choices=MODELS, null=True)
    name = models.CharField(max_length=100, null=True)
    mac = models.CharField(max_length=17, unique=True)
    call_home = models.BooleanField(default=False)
    rate = models.FloatField(null=True)
    public_key = models.CharField(max_length=700)
    essid = models.CharField(max_length=200, null=True)
    register_time = models.DateTimeField(null=True, default=datetime.datetime.now())
    sensor_ip = models.GenericIPAddressField(protocol='IPv4', null=True)
    department = models.ForeignKey(Departments, null=True)

    def __str__(self):
        return "%s" % self.mac

    class Meta:
        db_table = 'sensors'


class Brands(models.Model):
    brand_id = models.AutoField(primary_key=True,default='1')
    client = models.ForeignKey(Clients, blank=False, null=False)
    brand_name = models.CharField(max_length=100)
    register_date = models.DateTimeField(default=datetime.datetime.now())
    telephone = models.CharField(max_length=50)
    web_site = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=250)
    logo_url = models.URLField(null=True, blank=True)
    background_color = models.CharField(max_length=7, default='#ffffff')
    foreground_color = models.CharField(max_length=7, default='#ffffff')
    background_img = models.ImageField(upload_to='media')
    ttf_font = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    promotion_enable = models.BooleanField(default=False)
    
    def __str__(self):
        return "%s: %s" % self.brand_name

    def fullname(self):
        return "%s: %s" % self.brand_name

    class Meta:
        db_table = 'brands'


class PromotionsTypes(models.Model):
    promotion_type_id = models.AutoField(primary_key=True,default='1')
    promotion_type_name = models.CharField(max_length=50,default='default')
    description = models.CharField(max_length=100)

    def __str__(self):
        return "%s: %s" % self.promotion_type_name

    def fullname(self):
        return "%s: %s" % self.promotion_type_name

    class Meta:
        db_table = 'promotions_types'


class PromotionsFilters(models.Model):
    promotion_filter_id = models.AutoField(primary_key=True,default='1')
    promotion_filter_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return "%s: %s" % self.promotion_filter_name

    def fullname(self):
        return "%s: %s" % (self.promotion_filter_name)

    class Meta:
        db_table = 'promotions_filters'


class PromotionsLoyalties(models.Model):
    promotion_loyalty_id = models.AutoField(primary_key=True,default='1')
    promotion_loyalty_name = models.CharField(max_length=50)
    check_in_number = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    description = models.CharField(max_length=100)

    def __str__(self):
        return "%s: %s" % (self.promotion_loyalty_name)

    def fullname(self):
        return "%s: %s" % (self.promotion_loyalty_name)

    class Meta:
        db_table = 'promotions_loyalties'


class PromotionsSpecials(models.Model):
    promotion_special_id = models.AutoField(primary_key=True,default='1')
    promotion_special_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    def __str__(self):
        return "%s: %s" % (self.promotion_special_name)

    def fullname(self):
        return "%s: %s" % (self.promotion_special_name)

    class Meta:
        db_table = 'promotions_specials'



class Promotions(models.Model):
    promotion_id = models.AutoField(primary_key=True,default='1')
    client = models.ForeignKey(Clients, blank=False, null=False)
    promotion_name = models.CharField(max_length=100)
    register_date = models.DateTimeField(default=datetime.datetime.now())   
    description = models.TextField()
    short_description  = models.CharField(max_length=100)
    long_description = models.TextField()
    url = models.URLField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    active = models.BooleanField(default=True)   
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=True)
    sunday = models.BooleanField(default=True)
    img_url = models.URLField(max_length=200, null=True, blank=True)
    email_send = models.BooleanField(default=True)
    expiration_time_range = models.DateTimeField(default=datetime.datetime.now())   
    promotion_type = models.ForeignKey(PromotionsTypes, null=True)
    promotion_filter = models.ManyToManyField(PromotionsFilters)

    def __unicode__(self):
        return "%s" % self.promotion_name

    class Meta:
        db_table = 'promotions'


class PromotionsImpacts(models.Model):
    promotion = models.ForeignKey(Promotions)
    client = models.ForeignKey(Clients)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    impact_time = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())
    promo_code = models.CharField(max_length=200, null=True, blank=True)
    check_in = models.BooleanField(default=False)
    check_in_number = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    check_in_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'promotions_impacts'
