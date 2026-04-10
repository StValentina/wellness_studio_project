from django.core.validators import MinValueValidator
from django.db import models

from studio_classes.choices import LevelClassChoices


# Create your models here.
class StudioClass(models.Model):
    class_title = models.CharField(max_length=100)
    class_description = models.TextField()
    level = models.CharField(
        max_length=20,
        choices=LevelClassChoices.choices,
        default=LevelClassChoices.ALL_LEVELS,
    )
    duration_minutes = models.PositiveIntegerField(
        validators=[MinValueValidator(30)],
    )
    class_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    hall_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
    )
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
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
        related_name='studio_classes',  # tag.studio_classes.all()
    )
    instructor = models.ForeignKey(
        'accounts.AccountUser',
        on_delete=models.CASCADE,
        related_name='studio_classes',  #user.studio_classes.all()
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.class_title

'''
евентуално валидатор за минутите
'''

class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return self.name

