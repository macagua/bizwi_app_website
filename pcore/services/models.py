from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import pytz
from django.utils.translation import ugettext_lazy as _


# Users Models
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, is_admin, **extra_fields):
        now = datetime.now()
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
    date_joined = models.DateTimeField(default=datetime.utcnow(), editable=False)
    lang = models.CharField(max_length=2, default='es', blank=False, null=False)

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

    class Meta:
        db_table = 'custom_users'


# class basic
class Countries(models.Model):
    country_id = models.IntegerField(primary_key=True, null=False)
    country = models.CharField(max_length=200)

    class Meta:
        db_table = 'countries'
        
    def __unicode__(self):
        return "%s" % self.country


class Cities(models.Model):
    city_id = models.IntegerField(primary_key=True, null=False)
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cities'
    
    def __unicode__(self):
        return "%s" % self.city


class Regions(models.Model):
    region_id = models.IntegerField(primary_key=True, null=False)
    region = models.CharField(max_length=100)

    class Meta:
        db_table = 'regions'
        
    def __unicode__(self):
        return "%s" % self.region


# class business logic
class Employees(CustomUser):
    language = models.CharField(max_length=2, blank=False, null=True) # default lang client
    is_client_admin = models.BooleanField(default=False)
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


class Clients(CustomUser):
    client_id = models.CharField(primary_key=True, max_length=10, null=False, blank=False)
    client_name = models.CharField(max_length=100, null=True, blank=True)
    code_crm = models.CharField(max_length=10, null=False, blank=False)
    telephone = models.CharField(max_length=50)
    web_site = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=250)
    logo_url = models.URLField(null=True, blank=True)
    background_color = models.CharField(max_length=7, default='#ffffff')
    foreground_color = models.CharField(max_length=7, default='#ffffff')
    background_img = models.URLField(null=True, blank=True)
    ttf_font = models.CharField(max_length=100, null=True, blank=True)
    promotion_enable = models.BooleanField(default=False)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    photo_url = models.URLField(null=True, blank=True)
    facebook_id = models.BigIntegerField(null=True, blank=True, default=0)
    facebook_link = models.URLField(null=True, blank=True, default=None)
    facebook_fanpage = models.URLField(null=True, blank=True)
    facebook_merchant_id = models.CharField(max_length=250)
    twitter_account = models.CharField(max_length=250)
    gplus_id = models.CharField(max_length=30, null=True, blank=True, default=None)
    language = models.CharField(max_length=10, null=True, blank=True)
    locale = models.CharField(max_length=10, null=True, blank=True)
    timezone = models.CharField(max_length=255, choices=[(x, x) for x in pytz.common_timezones])

    class Meta:
        db_table = 'clients'

    def is_client(self):
        return True


class StoreTags(models.Model):
    store_tag_id = models.CharField(max_length=10, primary_key=True)
    tag_name = models.CharField(max_length=255)
    store_id = models.ForeignKey('Stores', blank=True, null=True)

    class Meta:
        db_table = 'store_tags'

    def __unicode__(self):
        return "%s" % self.tag_name


class Stores(models.Model):
    store_id = models.CharField(max_length=10, primary_key=True)
    client = models.ForeignKey('Clients', blank=False, null=False)
    store_name = models.CharField(max_length=100)
    register_date = models.DateTimeField(default=datetime.utcnow())
    region = models.ForeignKey('Regions', blank=True, null=True)
    country = models.ForeignKey('Countries', blank=True, null=True)
    city = models.ForeignKey('Cities', blank=True, null=True)
    address = models.CharField(max_length=200)
    geoloc_point = models.DecimalField(decimal_places=2, max_digits=5)
    distance_threshold = models.DecimalField(decimal_places=2, max_digits=5)
    geoloc_poly = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=50)
    web_site = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=250)
    logo_url = models.URLField(null=True, blank=True)
    background_color = models.CharField(max_length=7, default='#ffffff')
    foreground_color = models.CharField(max_length=7, default='#ffffff')
    backgroud_img = models.ImageField(upload_to='media')
    ttf_font = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    promotion_enable = models.BooleanField(default=False)
    employee = models.ManyToManyField(Employees)
    
    def __str__(self):
        return "%s" % self.store_name

    class Meta:
        db_table = 'stores'
        

class Departments(models.Model):
    department_id = models.CharField(max_length=10, primary_key=True)
    store_id = models.ForeignKey('Stores', blank=False, null=False)
    department_name = models.CharField(max_length=100,default='all')
    register_date = models.DateTimeField(default=datetime.utcnow())
    geoloc_point = models.DecimalField(decimal_places=2, max_digits=5)
    distance_threshold = models.DecimalField(decimal_places=2, max_digits=5)
    geoloc_poly = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "%s:" % self.department_name

    class Meta:
        db_table = 'departments'
