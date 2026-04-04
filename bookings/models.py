from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(
        'accounts.AccountUser',
        on_delete=models.CASCADE
    )
    booked_class = models.ForeignKey(
        'studio_classes.StudioClass',
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'booked_class'],
                name='unique_user_booking',
            )
        ]

    def __str__(self):
        return self.booked_class.class_title
