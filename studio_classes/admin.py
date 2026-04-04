from django.contrib import admin

from studio_classes.models import StudioClass


# Register your models here.


@admin.register(StudioClass)
class StudioClassAdmin(admin.ModelAdmin):
    pass