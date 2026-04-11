from django.contrib import admin

from services.models import Service


# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_title','service_description',]
    search_fields = ['service_title',]