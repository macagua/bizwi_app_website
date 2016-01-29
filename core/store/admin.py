from django.contrib import admin
from core.store.models import Stores
from core.store.models import Cities
from core.store.models import Countries
from core.store.models import Locations
from core.store.models import Departments


admin.site.register(Stores)
admin.site.register(Cities)
admin.site.register(Countries)
admin.site.register(Locations)
admin.site.register(Departments)


