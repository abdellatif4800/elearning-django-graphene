import graphene


class CourseInput(graphene.InputObjectType):
    question = graphene.String()
    type = graphene.String()
