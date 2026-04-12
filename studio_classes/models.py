from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from studio_classes.choices import LevelClassChoices


# Create your models here.
class StudioClass(models.Model):
    class_title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5),
        ]
    )
    class_description = models.TextField(
        max_length=1000,
        validators=[
            MinLengthValidator(20),
        ]
    )
    level = models.CharField(
        max_length=20,
        choices=LevelClassChoices.choices,
        default=LevelClassChoices.ALL_LEVELS,
    )
    duration_minutes = models.PositiveIntegerField(
        validators=[MinValueValidator(5)],
    )
    class_date = models.DateField()
    start_time = models.TimeField()
    hall_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
    )
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(2)],
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    studio_class_service = models.ManyToManyField(
        'services.Service',
        related_name='studio_classes',
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='studio_classes',
    )
    instructor = models.ForeignKey(
        'accounts.AccountUser',
        on_delete=models.SET_NULL,
        related_name='studio_classes',
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.class_title

class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            MinLengthValidator(3),
        ]
    )

    def __str__(self):
        return self.name

