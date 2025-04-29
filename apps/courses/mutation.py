import graphene

# from . import types as myTypes
# from . import forms as myForms
# from . import models as myModels
# from . import inputs as myInputs
from django.contrib.auth.models import User

from graphene_django.forms.mutation import DjangoFormMutation, DjangoModelFormMutation


class QuestionMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        in1 = graphene.String()

    # The class attributes define the response of the mutation
    question = graphene.String()

    def mutate(root, info, text, id):
        question = myModels.Question(id="123", ques="asd?", ques_type="tf")
        question.text = text
        # question.save()

        return QuestionMutation(question=question)
