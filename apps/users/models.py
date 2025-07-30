from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Meta:
        app_label = "users"

    class Role(models.TextChoices):
        AUTHOR = "AUT", "Author"
        ADMIN = "ADM", "Admin"
        STUDENT = "STU", "Student"
        INSTRUCTOR = "INS", "Instructor"
        GUST = "GUE", "Guest"
        REVIEWER = "REV", "Reviewer"

    role = models.CharField(choices=Role.choices, null=False)
    # age = models.PositiveIntegerField(blank=True, null=True)
    # is_verified = models.BooleanField(default=False)
