from datetime import time, date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from reviews.models import Review
from studio_classes.models import StudioClass

UserModel = get_user_model()

class ClassReviewListTests(TestCase):

    def test_returns_only_reviews_for_given_class(self):
        user = UserModel.objects.create_user(
            email='testuser@test.bg',
            password='test@#123'
        )

        class1 = StudioClass.objects.create(
            class_title='Class 1',
            instructor=user,
            duration_minutes=60,
            start_time=time(10, 0),
            class_date=date.today(),
            hall_number=1,
            capacity=10,
            price=20,
        )

        review1 = Review.objects.create(
            review_class=class1,
            user=user,
            rating=5,
            review_text='Great'
        )

        url = reverse('class-reviews', kwargs={'pk': class1.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(review1, response.context['reviews'])


