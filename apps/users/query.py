import graphene
from . import types as myTypes
from . import forms as myForms
from . import models as myModels
from . import inputs as myInputs
from django.contrib.auth.models import User

from graphene_django.forms.mutation import DjangoFormMutation, DjangoModelFormMutation


class Mutation(graphene.ObjectType):
    pass
