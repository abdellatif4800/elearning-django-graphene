from django.db import models
import graphene
from graphene_django import DjangoObjectType, DjangoListField
from django.contrib.auth.models import User

from . import models as myModels


# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = ("id", "username", "email", "is_staff")


class ManageQuizType(DjangoObjectType):
    class Meta:
        model = myModels.Quiz
        exclude = ("questions", "questions_count")


class ListQuizType(DjangoObjectType):
    class Meta:
        model = myModels.Quiz
        fields = (
            "name",
            "author",
            "category",
            "questions_count",
        )


class AnswerType(DjangoObjectType):
    class Meta:
        model = myModels.Answer


class ManageQuestionType(DjangoObjectType):
    class Meta:
        model = myModels.Question


class SubmittedAnswersType(DjangoObjectType):
    class Meta:
        model = myModels.Users_answers
        exclude = ("score",)


class ScoresType(DjangoObjectType):
    class Meta:
        model = myModels.Score
        fields = ("id", "quiz", "user", "score", "submitted_at")
