from django.contrib import admin
#from .models import Countries, Cities, Regions, Employees, Clients, Stores, Tags, Categories, Departments, Sensors, Brands, PromotionsTypes, PromotionsFilters, PromotionsLoyalties, PromotionsSpecials, Promotions, PromotionsImpacts
from .models import BrandStyle, BrandTags, Brands, Categories, Cities, Countries, \
    CustomerCategories, CustomerStyles, CustomerTags, Customers, Departments, Districts, \
    LocationTags, Locations, Sensor, StoreStyle, Stores

class BrandsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['customer', 'brand_name', 'description', 'url', 'age_range', 'is_active']}),
        ('Social networks', {'fields': ['fb_fanpage', 'fb_merchant_id', 'google_id', 'instagram_id', 'twitter_id', 'gplus_id']}),
        ('More details', {'fields': ['gtin', 'creation_date', 'last_access', 'mod_date']}),
    ]
    list_display = ('customer', 'brand_name', 'is_active')
    list_filter = ['customer', 'brand_name', 'is_active']


class CustomerCategoriesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['customer', 'category']}),
    ]
    list_display = ('customer', 'category')
    list_filter = ['customer']


class CustomersAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['customer_name', 'business_name', 'code_crm', 'prefix', 'description', 'telephone', 'email', 'url', 'age_range', 'is_active']}),
        ('Social networks', {'fields': ['fb_fanpage', 'fb_merchant_id', 'twitter_id', 'instagram_id', 'google_id', 'gplus_id']}),
        ('More details', {'fields': ['lang', 'timezone', 'locale', 'brand_enabled', 'gtin', 'creation_date', 'last_access', 'mod_date']}),
    ]
    list_display = ('code_crm', 'customer_name', 'business_name', 'telephone', 'email', 'url')
    list_filter = ['customer_name', 'business_name', 'is_active']


class StoresAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['customer', 'store_name', 'description', 'phone', 'address', 'url', 'is_active']}),
        ('More details', {'fields': ['timezone', 'lang', 'creation_date', 'last_access', 'mod_date']}),
    ]
    list_display = ('customer', 'store_name', 'phone', 'url', 'is_active')
    list_filter = ['customer', 'store_name', 'is_active']

admin.site.register(BrandStyle)
admin.site.register(BrandTags)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Categories)
admin.site.register(Cities)
admin.site.register(Countries)
admin.site.register(CustomerCategories, CustomerCategoriesAdmin)
admin.site.register(CustomerStyles)
admin.site.register(CustomerTags)
admin.site.register(Customers, CustomersAdmin)
admin.site.register(Departments)
admin.site.register(Districts)
admin.site.register(LocationTags)
admin.site.register(Locations)
admin.site.register(Sensor)
admin.site.register(StoreStyle)
admin.site.register(Stores, StoresAdmin)
#admin.site.register(Regions)
#admin.site.register(Employees)
#admin.site.register(Tags)
#admin.site.register(PromotionsTypes)
#admin.site.register(PromotionsFilters)
#admin.site.register(PromotionsLoyalties)
#admin.site.register(PromotionsSpecials)
#admin.site.register(Promotions)
#admin.site.register(PromotionsImpacts)
