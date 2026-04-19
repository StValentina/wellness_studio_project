from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.autoreload import logger

from .models import Booking
from .tasks import send_booking_confirmation_email


@receiver(post_save, sender=Booking)
def booking_created_send_email(sender, instance, created, **kwargs):
    if created:
        try:
            send_booking_confirmation_email.delay(
                instance.user.email,
                instance.booked_class.class_title,
            )
        except Exception as e:
            logger.error(f"Failed to queue booking email: {e}")