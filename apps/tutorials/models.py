from django.db import models
from django.contrib.auth.models import Group, User


from pydantic import BaseModel, HttpUrl, ValidationError
from typing import List
from django.core import serializers


class Tutorial(models.Model):
    name = models.CharField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.name


class Tutorial_Unit(models.Model):
    tutorial = models.ForeignKey(
        Tutorial, on_delete=models.CASCADE, related_name="units")
    title = models.CharField(default="Introduction")
    content = models.TextField()
    unit_number = models.IntegerField(unique=True)
    images = models.URLField(null=True)

    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if self.images:
    #         # raises ValidationError if invalid
    #         try:
    #             validate = ImageSchema(**self.images)
    #             print("img", validate)
    #             super().save(*args, **kwargs)
    #         except ValidationError as e:
    #             print("image Validation error:")
    #             print(e)
