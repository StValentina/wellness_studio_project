from datetime import time

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from bookings.models import Booking
from studio_classes.models import StudioClass

UserModel = get_user_model()

class BookingTests(TestCase):

    def test_creates_booking(self):
        user = UserModel.objects.create_user(
            email='test1@test.bg',
            password='1234'
        )

        self.client.login(email='test1@test.bg', password='1234')

        studio_class = StudioClass.objects.create(
            class_title='Test Class',
            instructor=user,
            duration_minutes=60,
            start_time=time(10, 0),
            hall_number=1,
            capacity=10,
            price=20,
        )

        url = reverse('book-class', kwargs={'pk': studio_class.pk})

        self.client.post(url)

        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.user, user)
        self.assertEqual(booking.booked_class, studio_class)

    def test_booking_requires_login(self):
        user = UserModel.objects.create_user(
            email='test2@test.bg',
            password='test@#123'
        )

        studio_class = StudioClass.objects.create(
            class_title='Test Class',
            instructor=user,
            duration_minutes=60,
            start_time=time(10, 0),
            hall_number=1,
            capacity=10,
            price=20,
        )

        url = reverse('book-class', kwargs={'pk': studio_class.pk})

        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)

    def test_book_class_does_not_duplicate(self):
        user = UserModel.objects.create_user(
            email='test3@test.bg',
            password='1234'
        )

        self.client.login(email='test3@test.bg', password='1234')

        studio_class = StudioClass.objects.create(
            class_title='Test Class',
            instructor=user,
            duration_minutes=60,
            start_time=time(10, 0),
            hall_number=1,
            capacity=10,
            price=20,
        )

        Booking.objects.create(
            user=user,
            booked_class=studio_class
        )

        url = reverse('book-class', kwargs={'pk': studio_class.pk})

        self.client.post(url)

        self.assertEqual(Booking.objects.count(), 1)