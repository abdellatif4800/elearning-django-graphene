import graphene


class TutorialInput(graphene.InputObjectType):
    name = graphene.String()
    author = graphene.ID()
    # updated_at = graphene.DateTime()


class UnitInput(graphene.InputObjectType):
    tutorial = graphene.ID()
    title = graphene.String()
    content = graphene.String()
    unit_number = graphene.Int()
    images = graphene.String()
