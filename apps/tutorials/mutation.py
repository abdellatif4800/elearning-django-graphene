import graphene
from graphene_django.forms.mutation import DjangoFormMutation, DjangoModelFormMutation

from . import types as myTypes

# from . import forms as myForms
from . import models as myModels
from . import inputs as myInputs

from django.utils import timezone
from django.contrib.auth.models import User, Group


class CreateTutorial(graphene.Mutation):
    class Arguments:
        tutorial_data = myInputs.TutorialInput()

    tutorial = graphene.Field(myTypes.TutorialType)

    def mutate(root, info, **kwargs):
        data = kwargs["tutorial_data"]

        tutorial_instance = myModels.Tutorial(
            name=data["name"], created_at=timezone.now()
        )
        # print(tutorial_instance)
        if tutorial_instance:
            group_instance = Group.objects.create(
                name=f"Tutorial {data["name"]} Group")

            tutorial_instance.members_group = group_instance

            tutorial_instance.save()
            return CreateTutorial(tutorial=tutorial_instance)


class CreateUnit(graphene.Mutation):
    class Arguments:
        unit_data = myInputs.UnitInput()

    unit = graphene.Field(myTypes.UnitType)

    def mutate(root, info, **kwargs):
        data = kwargs["unit_data"]

        unit_instance = myModels.Tutorial_Unit(
            tutorial=myModels.Tutorial.objects.get(id=data['tutorial_id']),
            title=data['title'],
            content=data['content'],
            unit_number=data['unit_number'],
            images=data['images'],
        )
        # print(paragraph_instance)
        if unit_instance:
            unit_instance.save()
            return CreateUnit(unit=unit_instance)


class Tutorials_Mutation(graphene.ObjectType):
    create_tutorial = CreateTutorial.Field()
    create_unit = CreateUnit.Field()
