from django.conf.urls import url, include
from django.contrib import admin
from services import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/v1/auth/$', views.auth),

    url(r'^api/v1/customers/$', views.CustomersList.as_view()),
    #url(r'^api/v1/customer/(?P<pk>[0-9]+)$', views.CustomerDetail.as_view()),

    # Section User ( custom User )

    # url(r'^api/v1/user/(?P<user_id>\d+)$', views.custom_user),
    url(r'^api/v1/user/set_pass/(?P<id>\d+)$', views.set_password),

    url(r'^api/v1/customer/(?P<client_id>\d+)$', views.customer),

    # url(r'^api-dashboard/v1/employees_list/(?P<client_id>\d+)$', views.employees_list),

    # Create user admin of client
    url(r'^api/v1/create_client_admin/$', views.create_client_admin),

    # url(r'^api/v1/employees/$', views.EmployeeList.as_view()),
    # url(r'^api/v1/employee/(?P<pk>[0-9]+)$', views.EmployeeDetail.as_view()),

    # url(r'^api/v1/get_employee_context/(?P<id>[0-9]+)$', views.get_employee_context),

    # Stores by client_id
    url(r'^api/v1/stores_list/(?P<client_id>\d+)$', views.stores),
    url(r'^api/v1/stores/(?P<client_id>\d+)$', views.stores),



    url(r'^api/v1/stores/$', views.stores),
    url(r'^api/v1/store/(?P<pk>[0-9]+)$', views.StoreDetail.as_view()),


    # url(r'^api/v1/employee_admin/(?P<client_id>\d+)$', views.employee_admin),


    url(r'^api/v1/countries/$', views.CountriesList.as_view()),
    url(r'^api/v1/country/(?P<pk>[0-9]+)$', views.CountryDetail.as_view()),

    url(r'^api/v1/cities/$', views.CitiesList.as_view()),
    url(r'^api/v1/city/(?P<pk>[0-9]+)$', views.CityDetail.as_view()),

    # url(r'^api/v1/regions/$', views.RegionsList.as_view()),
    # url(r'^api/v1/region/(?P<pk>[0-9]+)$', views.RegionDetail.as_view()),

    # url(r'^api/v1/tags/$', views.TagsList.as_view()),
    # url(r'^api/v1/tag/(?P<pk>[0-9]+)$', views.TagDetail.as_view()),

    url(r'^api/v1/categories/$', views.CategoriesList.as_view()),
    url(r'^api/v1/category/(?P<pk>[0-9]+)$', views.CategoryDetail.as_view()),

    url(r'^api/v1/departments/$', views.DepartmentsList.as_view()),
    url(r'^api/v1/department/(?P<pk>[0-9]+)$', views.DepartmentDetail.as_view()),

    url(r'^api/v1/sensors/$', views.SensorList.as_view()),
    url(r'^api/v1/sensor/(?P<pk>[0-9]+)$', views.SensorDetail.as_view()),

    url(r'^api/v1/brands/$', views.BrandsList.as_view()),
    url(r'^api/v1/brand/(?P<pk>[0-9]+)$', views.BrandDetail.as_view()),

    # url(r'^api/v1/promotionstypes/$', views.PromotionsTypesList.as_view()),
    # url(r'^api/v1/promotiontypes/(?P<pk>[0-9]+)$', views.PromotionTypeDetail.as_view()),

    # url(r'^api/v1/promotionsfilters/$', views.PromotionsFiltersList.as_view()),
    # url(r'^api/v1/promotionfilter/(?P<pk>[0-9]+)$', views.PromotionFilterDetail.as_view()),

    # url(r'^api/v1/promotionsloyalties/$', views.PromotionsLoyaltiesList.as_view()),
    # url(r'^api/v1/promotionloyalty/(?P<pk>[0-9]+)$', views.PromotionLoyaltyDetail.as_view()),

    # url(r'^api/v1/promotionsspecials/$', views.PromotionsSpecialsList.as_view()),
    # url(r'^api/v1/promotionspecial/(?P<pk>[0-9]+)$', views.PromotionSpecialDetail.as_view()),

    # url(r'^api/v1/promotions/$', views.PromotionsList.as_view()),
    # url(r'^api/v1/promotion/(?P<pk>[0-9]+)$', views.PromotionDetail.as_view()),

    # url(r'^api/v1/promotionsimpacts/$', views.PromotionsImpactsList.as_view()),
    # url(r'^api/v1/promotionimpact/(?P<pk>[0-9]+)$', views.PromotionImpactDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
