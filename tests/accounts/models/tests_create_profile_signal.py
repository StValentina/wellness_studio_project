from unittest import TestCase

from django.contrib.auth import get_user_model

from accounts.models import Profile

UserModel = get_user_model()

class CreateProfileSignalTest(TestCase):

    def test_create_profile_signal(self):
        self.assertEqual(Profile.objects.count(), 0)

        user = UserModel.objects.create_user(
            email='testuser@test.bg',
            password='test@#123'
        )

        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(user.profile.user, user)
