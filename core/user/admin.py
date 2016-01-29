from django.contrib import admin
from core.user.models import Users
from core.user.models import AuthSocial
from core.user.models import UsersIdentity
from core.user.models import UsersProfile


admin.site.register(Users)
admin.site.register(AuthSocial)
admin.site.register(UsersProfile)
admin.site.register(UsersIdentity)
