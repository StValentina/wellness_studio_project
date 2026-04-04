from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Review(models.Model):
    review = models.TextField()
    user = models.ForeignKey(
        'accounts.AccountUser',
        on_delete=models.CASCADE
    )
    review_class = models.ForeignKey(
        'studio_classes.StudioClass',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review
