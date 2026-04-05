from django.contrib import admin

from accounts.models import Profile, AccountUser


# Register your models here.

@admin.register(AccountUser)
class AccountUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'date_joined',)
    search_fields = ('email',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name',)
    search_fields = ('user__email',)
    list_filter = ('role',)
