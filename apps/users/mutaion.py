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

    user = graphene.Field(myTypes.RegistrationType)

    def mutate(root, info, **kwargs):
        user = User.objects.create_user(
            kwargs["first_name"], kwargs["email"], kwargs["password"]
        )
        print(user)

        return RegistrationMutation(user=user)
        # question = myModels.Question(id="123", ques="asd?", ques_type="tf")
        # question.text = text
        # # question.save()
        #
        # return QuestionMutation(question=question)
