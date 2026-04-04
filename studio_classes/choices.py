from django.db.models.enums import TextChoices


class LevelClassChoices(TextChoices):
    BEGINNER = 'Beginner', 'Beginner'
    INTERMEDIATE = 'Intermediate', 'Intermediate'
    ADVANCED = 'Advanced', 'Advanced'
    ALL_LEVELS = 'All Levels', 'All Levels'