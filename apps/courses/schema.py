import graphene
from django import forms

# from . import models as myModels
# from . import types as myTypes
# from . import forms as myForms
from . import mutation as myMutations
from graphene_django import DjangoObjectType, DjangoListField


class Query(graphene.ObjectType):
    get_course = graphene.String()


class Mutation(graphene.ObjectType):
    update_question = myMutations.QuestionMutation.Field()
