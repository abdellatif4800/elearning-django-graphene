import graphene
from django import forms
from graphene_django import DjangoListField
from graphene_django import DjangoObjectType, DjangoListField

from . import models as myModels
from . import types as myTypes
from . import mutation as myMutations


class Tutorial_Queries(graphene.ObjectType):
    retrieve_tutorial = graphene.Field(myTypes.TutorialType, id=graphene.Int())

    tutorials_per_category = DjangoListField(
        myTypes.TutorialType, category=graphene.String()
    )

    retrieve_unit = graphene.Field(myTypes.UnitType, id=graphene.Int())

    units_per_tutorial = DjangoListField(myTypes.UnitType, tutorial_id=graphene.Int())

    def resolve_retrieve_unit(root, info, **kwargs):
        target_unit = myModels.Tutorial_Unit.objects.get(id=kwargs["id"])
        print(target_unit)

        return target_unit

    def resolve_retrieve_tutorial(root, info, **kwargs):
        target_tut = myModels.Tutorial.objects.get(id=kwargs["id"])
        # print(target_tut.units_count)

        return target_tut

    def resolve_tutorials_per_category(root, info, **kwargs):
        tutorials = myModels.Tutorial.objects.filter(category=kwargs["category"])

        return tutorials

    def resolve_units_per_tutorial(root, info, **kwargs):
        units = myModels.Tutorial_Unit.objects.filter(
            tutorial=myModels.Tutorial.objects.get(id=kwargs["tutorial_id"])
        ).order_by("unit_number")

        return units
