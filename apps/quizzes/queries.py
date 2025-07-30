import graphene
from django import forms
from graphene_django import DjangoListField
from graphene_django import DjangoObjectType, DjangoListField

from . import models as myModels
from . import types as myTypes
from . import mutation as myMutations
from django.contrib.auth import get_user_model

User = get_user_model()


class Quiz_queries(graphene.ObjectType):
    quizzes_per_category = DjangoListField(
        myTypes.ListQuizType, category=graphene.String()
    )

    def resolve_quizzes_per_category(root, info, **kwargs):
        quizzis = [
            quiz
            for quiz in myModels.Quiz.objects.filter(category=kwargs["category"])
            if quiz.published == True
        ]

        return quizzis
