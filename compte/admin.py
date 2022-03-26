from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from compte.models import Shopper

admin.site.register(Shopper, UserAdmin)
