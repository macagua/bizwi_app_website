from django.contrib import admin
from .models import Employees, Clients, Stores, Tags, Brands, Departments, Promotions, PromotionsTypes


admin.site.register(Employees)

admin.site.register(Clients)

admin.site.register(Stores)

admin.site.register(Tags)

admin.site.register(Brands)

admin.site.register(Departments)

admin.site.register(Promotions)

admin.site.register(PromotionsTypes)


