import graphene
from graphene_django.forms.mutation import DjangoFormMutation, DjangoModelFormMutation

# from django.contrib.auth.models import User

from . import types as myTypes
from . import inputs as myInputs


from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationMutation(graphene.Mutation):
    class Arguments:
        userData = myInputs.UserInput()

    user = graphene.Field(myTypes.UserType)

    def mutate(root, info, **kwargs):
        user_data = kwargs["userData"]
        print(user_data["role"].value)
        user = User(
            username=user_data["username"],
            email=user_data["email"],
            role=user_data["role"].value,
        )
        user.set_password(
            user_data["password"],
        )

        if (
            user_data["role"].value == "AUT"
            or user_data["role"].value == "AD"
            or user_data["role"].value == "INS"
        ):
            user.is_staff = True
        user.save()
        return RegistrationMutation(user=user)


# Applying the decorator to a function
class usersMutation(graphene.ObjectType):
    registration = RegistrationMutation.Field()
