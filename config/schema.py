import graphene
from apps.users.mutation import usersMutation
from apps.users.queries import usersQueries
from apps.tutorials.mutation import Tutorials_Mutation
from apps.tutorials.queries import Tutorial_Queries


class Query(usersQueries, Tutorial_Queries, graphene.ObjectType):
    pass


class Mutation(usersMutation, Tutorials_Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
