import graphene

# from . import types as myTypes
# from . import forms as myForms
# from . import models as myModels
# from . import inputs as myInputs
from django.contrib.auth.models import User

from graphene_django.forms.mutation import DjangoFormMutation, DjangoModelFormMutation


class CourseMutation(graphene.Mutation):
    class Arguments:
        in1 = graphene.String()

    question = graphene.String()

    def mutate(root, info, text, id):
        question = myModels.Question(id="123", ques="asd?", ques_type="tf")
        question.text = text
        # question.save()

        return QuestionMutation(question=question)


class coursesMutation(graphene.ObjectType):
    update_question = CourseMutation.Field()
