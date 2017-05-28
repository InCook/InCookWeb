from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Account

# Define an inline admin descriptor for Account model
# which acts a bit like singleton
class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'accounts'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (AccountInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
