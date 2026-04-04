from django.db import models

# Create your models here.
class Service(models.Model):
    service_title = models.CharField(
        max_length=100,
        help_text='Keep it catchy! Maximum 100 characters.'
    )
    service_description = models.TextField(
        max_length=1000,
        help_text='Provide a detailed overview of what the service includes. Max 1000 characters.'
    )
    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_title

    """да се оправят снимките"""