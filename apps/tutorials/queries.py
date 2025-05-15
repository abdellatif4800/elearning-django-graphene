import graphene
from django import forms

from . import models as myModels
from . import types as myTypes

# from . import forms as myForms
from . import mutation as myMutations
from graphene_django import DjangoObjectType, DjangoListField


class Tutorial_Queries(graphene.ObjectType):
    get_tutorial = graphene.Field(myTypes.TutorialType, id=graphene.Int())
    get_unit = graphene.Field(myTypes.UnitType, id=graphene.Int())

    def resolve_get_unit(root, info, **kwargs):
        target_unit = myModels.Tutorial_Unit.objects.get(
            id=kwargs['id'])
        print(target_unit)

        return target_unit

    def resolve_get_tutorial(root, info, **kwargs):
        target_tut = myModels.Tutorial.objects.get(
            id=kwargs['id'])
        print(target_tut)

        return target_tut
