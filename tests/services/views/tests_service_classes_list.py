from datetime import time, date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from services.models import Service
from studio_classes.models import StudioClass

UserModel = get_user_model()

class ServiceClassesListTests(TestCase):

    def test_service_classes_for_particular_service(self):
        user1 = UserModel.objects.create_user(
            email='testuser1@test.bg',
            password='test1@#123',
        )

        user2 = UserModel.objects.create_user(
            email='testuser2@test.bg',
            password='test2@#123',
        )

        service1 = Service.objects.create(
            service_title='Service 1',
            service_description='Test description for service1',
        )

        service2 = Service.objects.create(
            service_title='Service 2',
            service_description='Test description for service1',
        )

        class1 = StudioClass.objects.create(
            class_title='Test Class 1',
            instructor=user1,
            duration_minutes=60,
            start_time=time(10, 0),
            class_date=date.today(),
            hall_number=1,
            capacity=10,
            price=20,
        )
        class1.studio_class_service.add(service1)

        class2 = StudioClass.objects.create(
            class_title='Test Class 2',
            instructor=user2,
            duration_minutes=45,
            start_time=time(12, 0),
            class_date=date.today(),
            hall_number=2,
            capacity=12,
            price=25,
        )
        class2.studio_class_service.add(service2)

        url = reverse('service-classes', kwargs={'pk': service1.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(class1, response.context['classes'])
        self.assertNotIn(class2, response.context['classes'])
