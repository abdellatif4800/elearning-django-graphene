import graphene


class ManageQuizInput(graphene.InputObjectType):
    name = graphene.String()
    category = graphene.String()
    published = graphene.Boolean()


class ManageQuestionInput(graphene.InputObjectType):
    quiz = graphene.ID()
    question = graphene.String()
    correct_answer = graphene.String()
    question_type = graphene.String()
    answers = graphene.List(graphene.String)


class UpdateQuestionInput(graphene.InputObjectType):
    question_id = graphene.ID()
    question = graphene.String()
    correct_answer = graphene.String()
    question_type = graphene.String()
    answers = graphene.List(graphene.String)


class UpdateMultipleQuestions(graphene.InputObjectType):
    questions = graphene.List(UpdateQuestionInput)


class MultipleQuestions(graphene.InputObjectType):
    questions = graphene.List(ManageQuestionInput)


class SubmittedAnswer(graphene.InputObjectType):
    question_id = graphene.Int()
    user_answer = graphene.String()


class ScoreInputs(graphene.InputObjectType):
    quiz_id = graphene.ID()
    user_id = graphene.ID()
    submitted_answers = graphene.List(SubmittedAnswer)
