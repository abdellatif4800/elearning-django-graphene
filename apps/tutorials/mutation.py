import graphene
from graphene_django.forms.mutation import DjangoFormMutation, DjangoModelFormMutation
from graphql import GraphQLError

from django.utils import timezone
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

from django.core import serializers

from . import types as myTypes
from . import models as myModels
from . import inputs as myInputs
from apps.users import helper as auth_helpers


class CreateTutorial(graphene.Mutation):
    class Arguments:
        tutorial_data = myInputs.ManageTutorialInput()

    tutorial = graphene.Field(myTypes.ManageTutorialType)

    @auth_helpers.verify_token
    @auth_helpers.verify_admin
    def mutate(root, info, **kwargs):
        data = kwargs["tutorial_data"]

        current_author = User.objects.get(id=kwargs["decoded_token"]["user_id"])

        tutorial_instance = myModels.Tutorial(
            name=data.get("name"),
            author=current_author,
            category=data["category"],
            published=data["published"],
            untis_count=0,
        )

        if tutorial_instance:
            # print(tutorial_instance)
            tutorial_instance.save()
            return CreateTutorial(tutorial=tutorial_instance)


class UpdateTutorial(graphene.Mutation):
    class Arguments:
        tutorial_id = graphene.Int(required=True)
        tutorial_data = myInputs.ManageTutorialInput()

    tutorial = graphene.Field(myTypes.ManageTutorialType)

    @auth_helpers.verify_token
    @auth_helpers.verify_admin
    def mutate(root, info, **kwargs):
        tutorial_id = kwargs["tutorial_id"]

        tutorial_data = kwargs["tutorial_data"]

        current_author = User.objects.get(id=kwargs["decoded_token"]["user_id"])

        target_tut = myModels.Tutorial.objects.get(id=tutorial_id)

        for key, value in tutorial_data.items():
            setattr(target_tut, key, value)

        target_tut.author = current_author
        target_tut.save()
        # print("target_tut", target_tut)
        target_tut.updated_at = timezone.now()
        return UpdateTutorial(tutorial=target_tut)


class DeleteTutorial(graphene.Mutation):
    class Arguments:
        tutorial_id = graphene.Int(required=True)

    delete_message = graphene.String()

    @auth_helpers.verify_token
    @auth_helpers.verify_admin
    def mutate(root, info, **kwargs):
        tutorial_id = kwargs["tutorial_id"]

        target_tut = myModels.Tutorial.objects.get(id=tutorial_id)
        target_tut.delete()
        return DeleteTutorial(
            delete_message=f"target tutorial {target_tut.name} deleted successfully!"
        )


class CreateUnit(graphene.Mutation):
    class Arguments:
        unit_data = myInputs.UnitInput()

    unit = graphene.Field(myTypes.UnitType)

    @auth_helpers.verify_token
    @auth_helpers.verify_admin
    def mutate(root, info, **kwargs):
        data = kwargs["unit_data"]
        units_per_tut = myModels.Tutorial_Unit.objects.filter(tutorial=data["tutorial"])

        unit_instance = myModels.Tutorial_Unit(
            tutorial=myModels.Tutorial.objects.get(id=data["tutorial"]),
            title=data["title"],
            content=data["content"],
            unit_number=data["unit_number"],
        )

        if unit_instance:
            unit_instance.save()
            return CreateUnit(unit=unit_instance)


class UpdateUnit(graphene.Mutation):
    class Arguments:
        unit_id = graphene.Int(required=True)
        unti_data = myInputs.UpdateUnitInput()

    unit = graphene.Field(myTypes.UnitType)

    @auth_helpers.verify_token
    @auth_helpers.verify_admin
    def mutate(root, info, **kwargs):
        unit_id = kwargs["unit_id"]
        unti_data = kwargs["unti_data"]

        target_unit = myModels.Tutorial_Unit.objects.get(id=unit_id)

        for key, value in unti_data.items():
            setattr(target_unit, key, value)

        target_unit.save()
        target_unit.updated_at = timezone.now()
        return UpdateUnit(unit=target_unit)


class DeleteUnit(graphene.Mutation):
    class Arguments:
        unit_id = graphene.Int(required=True)

    delete_message = graphene.String()

    def mutate(root, info, **kwargs):
        unit_id = kwargs["unit_id"]

        target_unit = myModels.Tutorial_Unit.objects.get(id=unit_id)
        target_unit.delete()
        return DeleteUnit(
            delete_message=f"target unit {target_unit.title} deleted successfully!"
        )


class Tutorials_Mutation(graphene.ObjectType):
    create_tutorial = CreateTutorial.Field()
    update_tutorial = UpdateTutorial.Field()
    delete_tutorial = DeleteTutorial.Field()
    create_unit = CreateUnit.Field()
    update_unit = UpdateUnit.Field()
    delete_unit = DeleteUnit.Field()
