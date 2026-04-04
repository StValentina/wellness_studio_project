from django.db.models.enums import TextChoices


class RoleChoices(TextChoices):
    HOST = 'Host', 'Host'
    PARTICIPANT = 'Participant', 'Participant'
    INSTRUCTOR = 'Instructor', 'Instructor'