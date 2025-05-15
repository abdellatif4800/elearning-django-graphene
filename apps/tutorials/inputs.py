import graphene


class TutorialInput(graphene.InputObjectType):
    name = graphene.String()


class ImageInput(graphene.InputObjectType):
    urls = graphene.String()
    alt_texts = graphene.String()


class UnitInput(graphene.InputObjectType):
    tutorial_id = graphene.ID(required=True)
    title = graphene.String(required=True)
    content = graphene.String(required=True)
    unit_number = graphene.Int(required=True)
    images = graphene.Field(ImageInput)
