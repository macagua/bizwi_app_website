from django.conf.urls import url
from django.contrib import admin
from services import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/countries/$', views.CountriesList.as_view()),
    url(r'^api/v1/country/(?P<pk>[0-9]+)$', views.CountryDetail.as_view()),

    url(r'^api/v1/cities/$', views.CitiesList.as_view()),
    url(r'^api/v1/city/(?P<pk>[0-9]+)$', views.CityDetail.as_view()),

    url(r'^api/v1/regions/$', views.RegionsList.as_view()),
    url(r'^api/v1/region/(?P<pk>[0-9]+)$', views.RegionDetail.as_view()),

    url(r'^api/v1/clients/$', views.ClientsList.as_view()),
    url(r'^api/v1/client/(?P<pk>[0-9]+)$', views.ClientDetail.as_view()),

    url(r'^api/v1/employees/$', views.EmployeeList.as_view()),
    url(r'^api/v1/employee/(?P<pk>[0-9]+)$', views.EmployeeDetail.as_view()),

    url(r'^api/v1/stores/$', views.StoresList.as_view()),
    url(r'^api/v1/store/(?P<pk>[0-9]+)$', views.StoreDetail.as_view()),

    url(r'^api/v1/tags/$', views.TagsList.as_view()),
    url(r'^api/v1/tag/(?P<pk>[0-9]+)$', views.TagDetail.as_view()),

    url(r'^api/v1/categories/$', views.CategoriesList.as_view()),
    url(r'^api/v1/category/(?P<pk>[0-9]+)$', views.CategoryDetail.as_view()),

    url(r'^api/v1/departments/$', views.DepartmentsList.as_view()),
    url(r'^api/v1/department/(?P<pk>[0-9]+)$', views.DepartmentDetail.as_view()),

    url(r'^api/v1/sensors/$', views.SensorsList.as_view()),
    url(r'^api/v1/sensor/(?P<pk>[0-9]+)$', views.SensorDetail.as_view()),

    url(r'^api/v1/brands/$', views.BrandsList.as_view()),
    url(r'^api/v1/brand/(?P<pk>[0-9]+)$', views.BrandDetail.as_view()),

    url(r'^api/v1/promotionstypes/$', views.PromotionsTypesList.as_view()),
    url(r'^api/v1/promotiontypes/(?P<pk>[0-9]+)$', views.PromotionTypeDetail.as_view()),

    url(r'^api/v1/promotionsfilters/$', views.PromotionsFiltersList.as_view()),
    url(r'^api/v1/promotionfilter/(?P<pk>[0-9]+)$', views.PromotionFilterDetail.as_view()),

    url(r'^api/v1/promotionsloyalties/$', views.PromotionsLoyaltiesList.as_view()),
    url(r'^api/v1/promotionloyalty/(?P<pk>[0-9]+)$', views.PromotionLoyaltyDetail.as_view()),

    url(r'^api/v1/promotionsspecials/$', views.PromotionsSpecialsList.as_view()),
    url(r'^api/v1/promotionspecial/(?P<pk>[0-9]+)$', views.PromotionSpecialDetail.as_view()),

    url(r'^api/v1/promotions/$', views.PromotionsList.as_view()),
    url(r'^api/v1/promotion/(?P<pk>[0-9]+)$', views.PromotionDetail.as_view()),

    url(r'^api/v1/promotionsimpacts/$', views.PromotionsImpactsList.as_view()),
    url(r'^api/v1/promotionimpact/(?P<pk>[0-9]+)$', views.PromotionImpactDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
