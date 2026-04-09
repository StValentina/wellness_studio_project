from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

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