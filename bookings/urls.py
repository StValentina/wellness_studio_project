from django.urls import path

from bookings.views import BookClassView, CancelBookingView, MyBookingsView

urlpatterns = [
    path('my-bookings/', MyBookingsView.as_view(), name='my-bookings'),
    path('book/<int:pk>/', BookClassView.as_view(), name='book-class'),
    path('cancel/<int:pk>/', CancelBookingView.as_view(), name='cancel-booking'),
]