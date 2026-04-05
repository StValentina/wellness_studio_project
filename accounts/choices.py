from django.db.models.enums import TextChoices


class RoleChoices(TextChoices):
    ADMIN = 'Admin', 'Admin'
    HOST = 'Host', 'Host'
    PARTICIPANT = 'Participant', 'Participant'
    INSTRUCTOR = 'Instructor', 'Instructor'