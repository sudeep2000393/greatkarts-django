from django.contrib import admin

# Register your models here.
from .models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'last_name',
                    'first_name', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    read_only_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
