from django.test import TestCase
from django.urls import reverse

from services.models import Service


class ServiceListViewTests(TestCase):

    def test_service_list_view_returns_200(self):
        url = reverse('list-services')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_service_list_view_uses_correct_template(self):
        url = reverse('list-services')

        response = self.client.get(url)

        self.assertTemplateUsed(response, 'services/list-services.html')

    def test_service_list_view_returns_services_in_context(self):
        Service.objects.create(
            service_title='Service 1',
            service_description='Test description 1',
        )
        Service.objects.create(
            service_title='Service 2',
            service_description='Test description 2',
        )

        url = reverse('list-services')

        response = self.client.get(url)

        self.assertIn('services', response.context)
        self.assertEqual(len(response.context['services']), 2)

    def test_service_list_view_orders_services_by_created_at(self):
        Service.objects.create(
            service_title='Abc',
            service_description='Test description 1',
        )
        Service.objects.create(
            service_title='Def',
            service_description='Test description 2',
        )

        url = reverse('list-services')

        response = self.client.get(url)
        services = list(response.context['services'])

        self.assertEqual(services[0].service_title, 'Abc')
        self.assertEqual(services[1].service_title, 'Def')