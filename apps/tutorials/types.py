from django.db import models
import graphene
from graphene_django import DjangoObjectType, DjangoListField
from django.contrib.auth.models import User

from . import models as myModels


class TutorialType(DjangoObjectType):
    class Meta:
        model = myModels.Tutorial


class ManageTutorialType(DjangoObjectType):
    class Meta:
        model = myModels.Tutorial
        exclude = ("units", "untis_count")


class UnitType(DjangoObjectType):
    class Meta:
        model = myModels.Tutorial_Unit
