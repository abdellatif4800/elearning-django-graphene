import graphene
import graphene_django
from . import models as myModels

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserType(graphene_django.DjangoObjectType):
    class Meta:
        model = User


class SigninType(graphene.ObjectType):
    token = graphene.String()
