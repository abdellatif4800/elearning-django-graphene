import graphene
from django import forms

from . import models as myModels
from . import types as myTypes
from . import forms as myForms
from . import mutaion as myMutations
from graphene_django import DjangoObjectType, DjangoListField


class Query(graphene.ObjectType):
    get_user = graphene.String()


class Mutation(graphene.ObjectType):
    registration = myMutations.RegistrationMutation.Field()
