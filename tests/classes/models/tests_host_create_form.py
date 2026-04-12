from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()

class OnlyHostCreateClassTests(TestCase):

    def test_only_host_create(self):
        user = UserModel.objects.create_user(
            email='testuser@test.bg',
            password='test@#123'
        )

        user.profile.role = 'Host'
        user.profile.save()

        self.client.login(email=user.email, password='test@#123')

        url = reverse('create-class')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_host_not_allow_to_create(self):
        user = UserModel.objects.create_user(
            email='testuser1@test.bg',
            password='test2@#123'
        )

        user.profile.role = 'Instructor'
        user.profile.save()

        self.client.login(email=user.email, password='test2@#123')

        url = reverse('create-class')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)