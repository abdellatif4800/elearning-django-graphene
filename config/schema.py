import graphene
from apps.users.mutation import usersMutation
from apps.users.queries import usersQueries

# ---------------------------------------------
from apps.tutorials.mutation import Tutorials_Mutation
from apps.tutorials.queries import Tutorial_Queries

# ---------------------------------------------
from apps.quizzes.mutation import Quizzes_Mutation
from apps.quizzes.queries import Quiz_queries


class Query(usersQueries, Tutorial_Queries, Quiz_queries, graphene.ObjectType):
    pass


class Mutation(
    usersMutation, Tutorials_Mutation, Quizzes_Mutation, graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
