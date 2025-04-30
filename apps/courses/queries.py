import graphene
from django import forms

from . import models as myModels
from . import types as myTypes

# from . import forms as myForms
from . import mutation as myMutations
from graphene_django import DjangoObjectType, DjangoListField


class coursesQueries(graphene.ObjectType):
    get_course = graphene.Field(myTypes.CourseType)

    def resolve_get_course(root, info, **kwargs):

        return myModels.CourseModel(id=123, title="title 1", content="content 1")
