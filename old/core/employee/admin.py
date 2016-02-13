from django.contrib import admin
from core.employee.models import Employees
from core.employee.models import Roles
from core.employee.models import Permissions
from core.employee.models import PermissionsRoles

admin.site.register(Employees)
admin.site.register(Permissions)
admin.site.register(Roles)
admin.site.register(PermissionsRoles)
