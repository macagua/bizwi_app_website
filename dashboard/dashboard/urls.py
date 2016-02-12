from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # index
    url(r'^$', views.index, name='index'),

    # login
    url(r'^dashboard/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),

    # Register URLS
    url(r'registration/client_admin/$', views.new_client_admin, name='new_client_admin'),

    url(r'registration/client_admin/confirm/(?P<username>\w+)/(?P<code>\w+)/$', views.confirm_client,
        name='confirm_client_admin'),
    url(r'registration/client/', views.new_client, name='new_client'),



    url(r'^employees/$', views.employees_list, name='employees_list'),
    # url(r'^employee_admin/$', views.employee_admin, name='employee_admin_new'),
    # url(r'^employee_admin/(?P<id_employee>\d+)/$', views.employee_admin, name='employee_admin'),
]
