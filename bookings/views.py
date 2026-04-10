from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView

from bookings.models import Booking
from studio_classes.models import StudioClass


# Create your views here.
class BookClassView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        studio_class = get_object_or_404(StudioClass, pk=pk)

        Booking.objects.get_or_create(
            user=request.user,
            booked_class=studio_class,
        )

        return redirect('my_profile', pk=pk)

class CancelBookingView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        studio_class = get_object_or_404(StudioClass, pk=pk)

        booking = Booking.objects.filter(
            user=request.user,
            booked_class=studio_class,
        )
        booking.delete()

        return redirect('my_profile', pk=pk)

class MyBookingsView(LoginRequiredMixin, TemplateView):
    template_name = 'bookings/my-bookings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = timezone.localdate()
        now_time = timezone.localtime().time()

        user_bookings = Booking.objects.filter(
            user=self.request.user
        ).select_related('booked_class')

        upcoming_bookings = []
        past_bookings = []

        for booking in user_bookings:
            booked_class = booking.booked_class

            if booked_class.class_date > today:
                upcoming_bookings.append(booking)
            elif booked_class.class_date < today:
                past_bookings.append(booking)
            else:
                if booked_class.start_time >= now_time:
                    upcoming_bookings.append(booking)
                else:
                    past_bookings.append(booking)

        upcoming_bookings.sort(
            key=lambda b: (b.booked_class.class_date, b.booked_class.start_time)
        )
        past_bookings.sort(
            key=lambda b: (b.booked_class.class_date, b.booked_class.start_time),
            reverse=True
        )

        context['upcoming_bookings'] = upcoming_bookings
        context['past_bookings'] = past_bookings

        return context