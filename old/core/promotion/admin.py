from django.contrib import admin
from core.promotion.models import Promotions
from core.promotion.models import PromotionsStatus
from core.promotion.models import PromotionsType


admin.site.register(PromotionsStatus)
admin.site.register(Promotions)
admin.site.register(PromotionsType)
