import graphene
from graphene_django.forms.mutation import DjangoFormMutation, DjangoModelFormMutation

from django.contrib.auth.models import User

from . import types as myTypes
from . import inputs as myInputs


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


# Applying the decorator to a function
class usersMutation(graphene.ObjectType):
    registration = RegistrationMutation.Field()
