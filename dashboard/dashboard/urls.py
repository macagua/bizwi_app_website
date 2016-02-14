from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # index
    url(r'^$', views.index, name='index'),

    # login
    url(r'^dashboard/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^dashboard/logout/$', views.logout, name='logout'),
    url(r'^done/$', views.done, name='done'),

    url(r'^statics/$', views.stats, name='stadistics'),

    # Profile user
    url(r'dashboard/user_profile/', views.user_profile, name='user_profile'),
    url(r'dashboard/settings/', views.settings, name='settings'),

    #url(r'dashboard/profile/(?P<id_client>\d+)/$', views.profile, name='profile'),


    # Register URLS
    url(r'registration/client_admin/$', views.new_client_admin, name='new_client_admin'),
    url(r'registration/client_admin/confirm/(?P<username>\w+)/(?P<code>\w+)/$', views.confirm_client,
        name='confirm_client_admin'),
    url(r'registration/client/', views.new_client, name='new_client'),

    # dashoard urls
    url(r'^stores/$', views.stores, name='stores'),

    # create basic data store
    url(r'^store/$', views.store, name='new_store'),

    url(r'^store/(?P<id_local>\d+)/$', views.store, name='store'),
    url(r'^dashboard/$', views.dashboard, name='home'),



    url(r'^employees/$', views.employees_list, name='employees_list'),
    url(r'^employee/$', views.employee, name='new_employee'),




    url(r'^employee/(?P<id_employee>\d+)/$', views.employee, name='employee'),
    url(r'^settings_employee/', views.settings_employee, name='settings_employee'),

    # Temporal URL
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^employee/$', views.brands, name='brands'),
    url(r'^sensors/$', views.sensors, name='sensors'),
    url(r'^promotions/$', views.promotions, name='promotions'),
    url(r'^brands/$', views.brands, name='brands'),
    url(r'^cities/$', views.cities, name='cities'),
    url(r'^countries/$', views.countries, name='countries'),
    url(r'^regions/$', views.regions, name='regions'),
    url(r'^tags/$', views.tags, name='tags'),
    url(r'^categories/$', views.categories, name='categories'),

]
