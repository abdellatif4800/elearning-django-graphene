import graphene
from django import forms

from . import models as myModels
from . import types as myTypes
from . import forms as myForms
from . import mutaion as myMutations
from graphene_django import DjangoObjectType, DjangoListField
from django.contrib.auth import authenticate, login
from .helper import generate_token


class usersQueries(graphene.ObjectType):
    signin = graphene.Field(
        myTypes.SigninType, username=graphene.String(), password=graphene.String()
    )

    def resolve_signin(root, info, **kwargs):
        username = kwargs["username"]
        password = kwargs["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            token = generate_token({"username": username})
            print(token)
            return myTypes.SigninType(token=token)
