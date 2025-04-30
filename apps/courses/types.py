from django.db import models
import graphene
from graphene_django import DjangoObjectType, DjangoListField
from . import models as myModels


class CourseType(DjangoObjectType):
    class Meta:
        model = myModels.CourseModel
