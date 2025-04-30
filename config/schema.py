import graphene
from apps.users.mutaion import usersMutation
from apps.users.queries import usersQueries
from apps.courses.mutation import coursesMutation
from apps.courses.queries import coursesQueries


class Query(usersQueries, coursesQueries, graphene.ObjectType):
    pass


class Mutation(usersMutation, coursesMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

print(schema)
