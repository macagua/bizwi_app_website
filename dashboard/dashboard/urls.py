from django.conf.urls import url
from django.contrib import admin
from dashboard import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employees/$', views.employees_list, name='employees_list'),
   # url(r'^employee_admin/$', views.employee_admin, name='employee_admin_new'),
   # url(r'^employee_admin/(?P<id_employee>\d+)/$', views.employee_admin, name='employee_admin'),
]
