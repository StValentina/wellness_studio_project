from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class FullNameTests(TestCase):

    def create_user(self):
        return UserModel.objects.create_user(
            email='testuser@test.bg',
            password='test@#123'
        )

    def test_get_full_name_with_first_and_last_name(self):
        user = self.create_user()
        user.profile.first_name = 'Ivan'
        user.profile.last_name = 'Ivanov'

        result = user.profile.get_full_name()

        self.assertEqual(result, 'Ivan Ivanov')

    def test_get_full_name_with_only_first_name(self):
        user = self.create_user()
        user.profile.first_name = 'Ivan'
        user.profile.last_name = ''

        result = user.profile.get_full_name()

        self.assertEqual(result, 'Ivan')

    def test_get_full_name_with_only_last_name(self):
        user = self.create_user()
        user.profile.first_name = ''
        user.profile.last_name = 'Ivanov'

        result = user.profile.get_full_name()

        self.assertEqual(result, 'Ivanov')

    def test_get_full_name_with_no_name(self):
        user = self.create_user()
        user.profile.first_name = ''
        user.profile.last_name = ''

        result = user.profile.get_full_name()

        self.assertEqual(result, '')