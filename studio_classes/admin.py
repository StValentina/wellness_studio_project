from django.contrib import admin

from studio_classes.models import StudioClass


# Register your models here.


@admin.register(StudioClass)
class StudioClassAdmin(admin.ModelAdmin):
    list_display = ['class_title','class_date', 'start_time', 'instructor']
    fieldsets = [
        (
            'Studio Class Information',
            {
                'fields': ['class_title', 'class_description', 'level', 'tags'],
            }
        ),
        (
            'Administrative Information',
            {
                'fields': ['class_date', 'start_time', 'duration_minutes', 'hall_number', 'capacity', 'price']
            }
        )
    ]

    list_filter = ['studio_class_service',]