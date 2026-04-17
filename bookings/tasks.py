from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_booking_confirmation_email(user_email, class_title):
    send_mail(
        subject='Booking Confirmation',
        message=f'Your booking for "{class_title}" was successful.',
        from_email='admin@wellnessstudio.com',
        recipient_list=[user_email],
        fail_silently=False,
    )