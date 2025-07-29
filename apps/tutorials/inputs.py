import graphene


class ManageTutorialInput(graphene.InputObjectType):
    name = graphene.String()
    category = graphene.String()
    published = graphene.Boolean()


class UnitInput(graphene.InputObjectType):
    tutorial = graphene.ID()
    title = graphene.String()
    content = graphene.String()
    unit_number = graphene.Int()


class UpdateUnitInput(graphene.InputObjectType):
    title = graphene.String()
    content = graphene.String()
    unit_number = graphene.Int()
