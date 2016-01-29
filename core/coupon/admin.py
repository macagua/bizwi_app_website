from django.contrib import admin
from core.coupon.models import Coupons
from core.coupon.models import CouponsStatus
from core.coupon.models import CouponsType

admin.site.register(Coupons)
admin.site.register(CouponsType)
admin.site.register(CouponsStatus)
