import graphene
import apps.users.schema as usersSchema
import apps.courses.schema as coursesSchema


class Query(usersSchema.Query, coursesSchema.Query, graphene.ObjectType):
    pass


class Mutation(usersSchema.Mutation, coursesSchema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

print(schema)
