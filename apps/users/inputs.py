import graphene
from .enums import RoleEnum
from .models import CustomUser


class UserInput(graphene.InputObjectType):
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()
    role = RoleEnum()
