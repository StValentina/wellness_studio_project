from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.test import TestCase

from services.models import Service


class ImageSizeServiceTests(TestCase):

    def test_image_size_under_5_mb(self):
        small_image = SimpleUploadedFile(
            'test.jpg',
            b'a' * (1024 * 1024),
            content_type='image/jpeg'
        )

        service = Service.objects.create(
            service_title='Yoga',
            service_description='Test description for this service.',
            image=small_image
        )

        service.full_clean()

        self.assertIsNotNone(service.image)

    def test_image_size_over_5_mb_raises_error(self):
        big_image = SimpleUploadedFile(
            'big.jpg',
            b'a' * (6 * 1024 * 1024),
            content_type='image/jpeg'
        )

        service = Service.objects.create(
            service_title='Yoga',
            service_description='Test description for this service.',
            image=big_image
        )

        with self.assertRaises(ValidationError):
            service.full_clean()