from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import pytz
from django.utils.translation import ugettext_lazy as _

# Users Models
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, is_admin, **extra_fields):
        now = datetime.utcnow()
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

GENDER_CHOICES_PROMOTION = (
    ('A', 'All'),
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
    # lang = models.CharField(max_length=2, default='es', blank=False, null=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    #def get_lang(self):
    #    return self.lang

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

class Employee(CustomUser):
    location = models.ForeignKey('Location', blank=True, null=True)
    language = models.CharField(max_length=2, default="en", blank=False, null=True)
    is_customer_admin = models.BooleanField(default=False)
    customer = models.ForeignKey('Customer', blank=True, null=True)
    confirmation_code = models.CharField(max_length=66, blank=True, null=True)

    class Meta:
        db_table = 'employee'

    def is_employee(self):
        return True


class Client(CustomUser):
Client_name: Cosmopolitan
Code _CRM: BIZ001
Client_id: (autoincrement)01
telephone: +34 55555555
web_site: URL
description: 
facebook_fanpage:
facebook_merchant_id
	twitter: twitter account
	logo_url
	background_color
	foreground_color
	backgroud_img
	ttf_font
	is_active: boolean
	promotion_enable
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    photo_url = models.URLField(null=True, blank=True)
    facebook_id = models.BigIntegerField(null=True, blank=True, default=0)
    facebook_link = models.URLField(null=True, blank=True, default=None)
    gplus_id = models.CharField(max_length=30, null=True, blank=True, default=None)
    timezone = models.CharField(max_length=10, null=True, blank=True)
    language = models.CharField(max_length=10, null=True, blank=True)
    locale = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'client'

    def is_client(self):
        return True


telephone: +34 55555555
web_site: URL
description: 
facebook_fanpage:
facebook_merchant_id
twitter: twitter account
(colo schema)
logo_url
background_color
foreground_color
backgroud_img
ttf_font
language: es|en
country: (país por defecto)
is_active: boolean
enable: (es activo para crear promociones)

Rango de edades
categoría y sub-categoría 
etiquetas adicionales para categorizar al cliente








class Vendor(models.Model):
    oui = models.CharField(max_length=17, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'vendor'

    def __unicode__(self):
        return "%s" % (self.name)


class SsidRegister(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return "%s" % (self.name)


class Device(models.Model):
    mac = models.CharField(max_length=17, unique=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=30, null=True, blank=True)
    family = models.CharField(max_length=30, null=True, blank=True)
    os_family = models.CharField(max_length=30, null=True, blank=True)
    os_ver = models.CharField(max_length=30, null=True, blank=True)
    first_seen = models.DateTimeField(default=datetime.utcnow())
    last_seen = models.DateTimeField(default=datetime.utcnow())
    vendor = models.ForeignKey(Vendor, null=True, blank=True)
    user_agent = models.CharField(max_length=500, null=True, blank=True)
    ssids = models.ManyToManyField(SsidRegister)
    client = models.ForeignKey(Client, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.mac)

    class Meta:
        db_table = 'device'


class LocationDeviceClient(models.Model):
    location = models.ForeignKey('Location')
    device = models.ForeignKey(Device)
    visits = models.IntegerField(default=1)
    last_login = models.DateTimeField(default=datetime.utcnow())

    def __str__(self):
        return "%s %s %s" % (self.location, self.device, self.visits)

    class Meta:
        db_table = 'location_device_client'


class Customer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    timezone = models.CharField(max_length=255, choices=[(x, x) for x in pytz.common_timezones])
    img_url = models.URLField(max_length=200, null=True, blank=True)
    cover_img_url = models.URLField(max_length=200, null=True, blank=True)
    uppercolor = models.CharField(max_length=7, default='#ffffff')
    lowercolor = models.CharField(max_length=7, default='#ffffff')

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        db_table = 'customer'


class Location(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(decimal_places=5, max_digits=7)
    longitude = models.DecimalField(decimal_places=5, max_digits=8)
    distance_threshold = models.DecimalField(decimal_places=2, max_digits=5)
    clients_devices = models.ManyToManyField(Device, through=LocationDeviceClient)
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return "%s: %s" % (self.customer, self.name)

    def fullname(self):
        return "%s: %s" % (self.customer, self.name)

    class Meta:
        db_table = 'location'


class MessageToCustomer(models.Model):
    sender = models.ForeignKey(Client)
    receiver = models.ForeignKey(Customer)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, editable=False)
    read = models.BooleanField(default=False)

    class Meta:
        db_table = 'message_to_customer'


class MessageToClient(models.Model):
    sender = models.ForeignKey(Customer)
    receiver = models.ForeignKey(Client)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, editable=False)
    read = models.BooleanField(default=False)

    class Meta:
        db_table = 'message_to_client'


class Application(models.Model):
    user_agent = models.CharField(max_length=200)
    url = models.URLField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    ver = models.CharField(max_length=30, null=True, blank=True)
    ua_ver = models.CharField(max_length=30, null=True, blank=True)
    device = models.ForeignKey(Device)

    class Meta:
        db_table = 'application'


class PromotionImpact(models.Model):
    promotion = models.ForeignKey('Promotion')
    client = models.ForeignKey(Client)
    impact_time = models.DateTimeField(null=True, blank=True, default=datetime.utcnow())
    promo_code = models.CharField(max_length=200, null=True, blank=True)
    check_in = models.BooleanField(default=False)
    check_in_number = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    check_in_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'promotion_impact'


class PromotionImpactExternal(models.Model):
    promotion = models.ForeignKey('PromotionExternal')
    client = models.ForeignKey(Client)
    impact_time = models.DateTimeField(null=True, blank=True, default=datetime.utcnow())
    promo_code = models.CharField(max_length=200, null=True, blank=True)
    check_in = models.BooleanField(default=False)
    check_in_number = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    check_in_time = models.DateTimeField(null=True, blank=True)
    location = models.ForeignKey(Location)

    class Meta:
        db_table = 'promotion_impact_external'


class PromotionImpactSpecial(models.Model):
    promotion = models.ForeignKey('SpecialPromotion')
    client = models.ForeignKey(Client)
    impact_time = models.DateTimeField(null=True, blank=True, default=datetime.utcnow())
    promo_code = models.CharField(max_length=200, null=True, blank=True)
    check_in = models.BooleanField(default=False)
    check_in_number = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    check_in_time = models.DateTimeField(null=True, blank=True)
    next_check_in = models.DecimalField(max_digits=3, decimal_places=0, default=0)

    class Meta:
        db_table = 'promotion_impact_special'


class SpecialPromotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length=200, null=True, blank=True)
    required_check_ins = models.DecimalField(max_digits=3, decimal_places=0, default=3)
    active = models.BooleanField(default=True)
    img_url = models.URLField(max_length=200, null=True, blank=True)
    impact = models.ManyToManyField(Client, through=PromotionImpactSpecial)
    customer_id = models.ForeignKey(Customer)
    email_send = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        db_table = 'special_promotion'


class Promotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length=200, null=True, blank=True)
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
    location = models.ManyToManyField(Location)
    img_url = models.URLField(max_length=200, null=True, blank=True)
    impact = models.ManyToManyField(Client, through=PromotionImpact)
    # gender = models.CharField(max_length=1, default='A', choices=GENDER_CHOICES_PROMOTION, null=True, blank=True)
    # birthday = models.BooleanField(default=False)
    # locale = models.CharField(max_length=2, default='xx', null=True, blank=True)
    filter_str = models.CharField(max_length=200, default='', null=True, blank=True)
    special_promotion = models.ForeignKey(SpecialPromotion, blank=True, null=True)
    email_send = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        db_table = 'promotion'


class PromotionExternal(models.Model):
    customer = models.ForeignKey(Customer)
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length=200, null=True, blank=True)
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
    location = models.ManyToManyField(Location, through='PromotionLocation')
    img_url = models.URLField(max_length=200, null=True, blank=True)
    impact = models.ManyToManyField(Client, through=PromotionImpactExternal)
    filter_str = models.CharField(max_length=200, default='', null=True, blank=True)
    email_send = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        db_table = 'promotion_external'


class PromotionLocation(models.Model):
    promotion = models.ForeignKey(PromotionExternal)
    location = models.ForeignKey(Location)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __unicode__(self):
        return "%s, %s - status: %s " % (self.promotion.name, self.location.name, self.status)

    def fullname(self):
        return "%s, %s" % (self.promotion.name, self.promotion.description)

MODELS = (
    ('TP-LINK TL-MR3020', 'MR-3020'),
    ('TP-LINK TL-WDR3600', 'WDR-3600'),
    ('TP-LINK TL-WR1043', 'WR-1043'),
    ('TP-LINK TL-MR3040', 'MR-3040'),
    ('TP-LINK AC1750', 'AC1750'),
)


class Sensor(models.Model):
    sid = models.CharField(max_length=120, unique=True)
    mac = models.CharField(max_length=17, unique=True)
    model = models.CharField(max_length=30, choices=MODELS, null=True)
    register_time = models.DateTimeField(null=True, default=datetime.utcnow())
    sensor_ip = models.GenericIPAddressField(protocol='IPv4', null=True)
    public_key = models.CharField(max_length=700)
    name = models.CharField(max_length=100, null=True)
    call_home = models.BooleanField(default=False)
    essid = models.CharField(max_length=200, null=True)
    rate = models.FloatField(null=True)
    location = models.ForeignKey(Location, null=True)

    def __str__(self):
        return "%s" % (self.mac)

    class Meta:
        db_table = 'sensor'


class Ratio(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    time = models.FloatField()
    sensor = models.ForeignKey(Sensor)

    class Meta:
        db_table = 'ratio'


class Counter(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    time = models.FloatField()
    sensor = models.ForeignKey(Sensor)

    class Meta:
        db_table = 'counter'