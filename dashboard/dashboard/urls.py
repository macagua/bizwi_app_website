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

    # Register URLS
    url(r'registration/client_admin/$', views.new_client_admin, name='new_client_admin'),
    url(r'registration/client_admin/confirm/(?P<username>\w+)/(?P<code>\w+)/$', views.confirm_client,
        name='confirm_client_admin'),
    url(r'registration/client/', views.new_client, name='new_client'),

    # dashoard urls
    url(r'^stores/$', views.stores, name='stores'),

    # create basic data store
    url(r'^store/$', views.new_store, name='new_store'),

    # style data store
    url(r'^store_style/$', views.store_style, name='store_style'),

    # location data store
    url(r'^store_location/$', views.store_location, name='store_location'),

    url(r'^store/(?P<id_local>\d+)/$', views.store, name='store'),
    url(r'^dashboard/$', views.dashboard, name='home'),

    url(r'^employees/$', views.employees_list, name='employees_list'),
    url(r'^employee/$', views.employee, name='new_employee'),
    url(r'^employee/(?P<id_employee>\d+)/$', views.employee, name='employee'),
    url(r'^settings_employee/', views.settings_employee, name='settings_employee'),




    url(r'^employees/$', views.employees_list, name='employees_list'),
    # url(r'^employee_admin/$', views.employee_admin, name='employee_admin_new'),
    # url(r'^employee_admin/(?P<id_employee>\d+)/$', views.employee_admin, name='employee_admin'),
]

