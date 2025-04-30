import graphene
from graphene_django import DjangoObjectType, DjangoListField
from . import models as myModels
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class SigninType(graphene.ObjectType):
    token = graphene.String()
