from graphene_django import DjangoObjectType, DjangoListField
from . import models as myModels
from django.contrib.auth.models import User


class RegistrationType(DjangoObjectType):
    class Meta:
        model = User
