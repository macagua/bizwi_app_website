from django.contrib import admin
from core.device.models import Devices
from core.device.models import Vendors

admin.site.register(Devices)
admin.site.register(Vendors)
