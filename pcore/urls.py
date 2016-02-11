from django.conf.urls import url
from django.contrib import admin
from services import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/employees/$', views.EmployeeList.as_view()),
    url(r'^api/v1/employee/(?P<pk>[0-9]+)$', views.EmployeeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
