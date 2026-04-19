from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from datetime import time, date
from reviews.models import Review
from studio_classes.models import StudioClass

UserModel = get_user_model()

class ReviewRatingTests(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='testuser@test.bg',
            password='test@#123'
        )

        self.studio_class = StudioClass.objects.create(
            class_title='Test Class',
            instructor=self.user,
            duration_minutes=60,
            start_time=time(10, 0),
            class_date=date.today(),
            hall_number=1,
            capacity=10,
            price=20,
        )

    def test_review_rating_valid(self):
        review = Review(
            review_text='Great class!',
            user=self.user,
            review_class=self.studio_class,
            rating=5
        )

        review.full_clean()

    def test_review_rating_below_min_should_raise(self):
        review = Review(
            review_text='Bad',
            user=self.user,
            review_class=self.studio_class,
            rating=0
        )

        with self.assertRaises(ValidationError):
            review.full_clean()

    def test_review_rating_above_max_should_raise(self):
        review = Review(
            review_text='Excellent!',
            user=self.user,
            review_class=self.studio_class,
            rating=6
        )

        with self.assertRaises(ValidationError):
            review.full_clean()

    def test_review_text_too_short_should_raise(self):
        review = Review(
            review_text='Hey',
            user=self.user,
            review_class=self.studio_class,
            rating=3
        )

        with self.assertRaises(ValidationError):
            review.full_clean()