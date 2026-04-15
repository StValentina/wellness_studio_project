from django.contrib import admin

from services.models import Service


# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_title', 'service_description', 'created_by', 'created_at', 'updated_by', 'updated_at']
    search_fields = ['service_title',]