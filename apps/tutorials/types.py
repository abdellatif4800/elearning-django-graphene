from django.db import models
import graphene
from graphene_django import DjangoObjectType, DjangoListField
from . import models as myModels


class TutorialType(DjangoObjectType):
    class Meta:
        model = myModels.Tutorial


class UnitType(DjangoObjectType):
    class Meta:
        model = myModels.Tutorial_Unit
