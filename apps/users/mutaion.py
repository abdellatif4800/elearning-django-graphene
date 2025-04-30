import graphene
from . import types as myTypes
from . import forms as myForms
from . import models as myModels
from . import inputs as myInputs
from django.contrib.auth.models import User

from graphene_django.forms.mutation import DjangoFormMutation, DjangoModelFormMutation


class RegistrationMutation(graphene.Mutation):
    class Arguments:
        userData = myInputs.UserInput()

    user = graphene.Field(myTypes.UserType)

    def mutate(root, info, **kwargs):
        user_data = kwargs["userData"]
        user = User.objects.create_user(
            user_data["first_name"], user_data["email"], user_data["password"]
        )

        return RegistrationMutation(user=user)


class usersMutation(graphene.ObjectType):
    registration = RegistrationMutation.Field()
