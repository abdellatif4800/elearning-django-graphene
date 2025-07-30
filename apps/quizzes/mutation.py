import graphene
from graphene_django.forms.mutation import DjangoFormMutation, DjangoModelFormMutation
from graphql import GraphQLError

from django.utils import timezone
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

from django.core import serializers

from . import types as myTypes
from . import models as myModels
from . import inputs as myInputs
from apps.users import helper as auth_helpers


class CreateQuiz(graphene.Mutation):
    class Arguments:
        quiz_data = myInputs.ManageQuizInput()

    quiz = graphene.Field(myTypes.ManageQuizType)

    @auth_helpers.verify_token
    @auth_helpers.verify_admin
    def mutate(root, info, **kwargs):
        data = kwargs["quiz_data"]

        current_author = User.objects.get(id=kwargs["decoded_token"]["user_id"])

        quiz_instance = myModels.Quiz(
            name=data.get("name"),
            author=current_author,
            category=data["category"],
            published=data["published"],
            questions_count=0,
        )

        if quiz_instance:
            # print(quiz_instance)
            quiz_instance.save()
            return CreateQuiz(quiz=quiz_instance)


class UpdateQuiz(graphene.Mutation):
    class Arguments:
        quiz_id = graphene.Int(required=True)
        quiz_data = myInputs.ManageQuizInput()

    quiz = graphene.Field(myTypes.ManageQuizType)

    @auth_helpers.verify_token
    @auth_helpers.verify_admin
    def mutate(root, info, **kwargs):
        quiz_id = kwargs["quiz_id"]

        quiz_data = kwargs["quiz_data"]

        current_author = User.objects.get(id=kwargs["decoded_token"]["user_id"])

        target_quiz = myModels.Quiz.objects.get(id=quiz_id)

        for key, value in quiz_data.items():
            setattr(target_quiz, key, value)

        target_quiz.author = current_author
        target_quiz.save()

        target_quiz.updated_at = timezone.now()
        return UpdateQuiz(quiz=target_quiz)


class DeleteQuiz(graphene.Mutation):
    class Arguments:
        quiz_id = graphene.Int(required=True)

    delete_message = graphene.String()

    @auth_helpers.verify_token
    @auth_helpers.verify_admin
    def mutate(root, info, **kwargs):
        quiz_id = kwargs["quiz_id"]

        target_quiz = myModels.Quiz.objects.get(id=quiz_id)
        target_quiz.delete()
        return DeleteQuiz(
            delete_message=f"quiz: {target_quiz.name} deleted successfully!"
        )


class CreateQuestions(graphene.Mutation):
    class Arguments:
        question_data = myInputs.MultipleQuestions()

    questions = graphene.List(myTypes.ManageQuestionType)
    # test_msg = graphene.String()

    @auth_helpers.verify_token
    @auth_helpers.verify_admin
    def mutate(root, info, **kwargs):
        data = kwargs["question_data"]

        questions_list = []
        for current_question in data["questions"]:
            current_instance = myModels.Question.objects.create(
                quiz=myModels.Quiz.objects.get(id=current_question["quiz"]),
                question=current_question["question"],
                correct_answer=current_question["correct_answer"],
                question_type=current_question["question_type"],
            )

            answers = [
                myModels.Answer(question=current_instance, answer=ans)
                for ans in current_question["answers"]
            ]
            myModels.Answer.objects.bulk_create(answers)

            questions_list.append(current_instance)
        return CreateQuestions(questions=questions_list)


class UpdateQuestions(graphene.Mutation):
    class Arguments:
        question_data = myInputs.UpdateMultipleQuestions()

    questions = graphene.List(myTypes.ManageQuestionType)
    # test = graphene.String()

    @auth_helpers.verify_token
    @auth_helpers.verify_admin
    def mutate(root, info, **kwargs):
        question_data = kwargs["question_data"]
        updated_questions = []
        for question in question_data["questions"]:
            target_question = myModels.Question.objects.get(id=question["question_id"])
            for key, value in question.items():
                if key != "question_id" and key != "answers":
                    setattr(target_question, key, value)

                if key == "answers":
                    answers = myModels.Answer.objects.filter(
                        question=question["question_id"]
                    )

                    answers_values = [ans.answer for ans in answers]
                    if answers_values != question["answers"]:
                        answers.delete()
                        new_answers = [
                            myModels.Answer(question=target_question, answer=ans)
                            for ans in question["answers"]
                        ]
                        myModels.Answer.objects.bulk_create(new_answers)
                        print(new_answers)

            target_question.updated_at = timezone.now()
            target_question.save()
            updated_questions.append(target_question)
        return UpdateQuestions(questions=updated_questions)
        # return UpdateQuestions(test="test")


class DeleteQuestion(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int(required=True)

    delete_message = graphene.String()

    def mutate(root, info, **kwargs):
        question_id = kwargs["question_id"]

        target_question = myModels.Question.objects.get(id=question_id)
        target_question.delete()
        return DeleteQuestion(
            delete_message=f"question: {target_question.question} deleted successfully!"
        )


class SubmitQuiz(graphene.Mutation):
    class Arguments:
        ScoreInputs = myInputs.ScoreInputs()

    score = graphene.Field(myTypes.ScoresType)
    submitted_answers = graphene.List(myTypes.SubmittedAnswersType)
    # test = graphene.String()

    @auth_helpers.verify_token
    def mutate(root, info, **kwargs):
        user_answers = kwargs["ScoreInputs"]["submitted_answers"]
        quiz_id = kwargs["ScoreInputs"]["quiz_id"]
        user_id = kwargs["ScoreInputs"]["user_id"]
        score = 0

        user_answers_instances = []

        socre_instance = myModels.Score.objects.create(
            quiz=myModels.Quiz.objects.get(id=quiz_id),
            user=myModels.User.objects.get(id=user_id),
            score=score,
        )

        for ans in user_answers:
            target_question = myModels.Question.objects.get(id=ans.question_id)
            is_correct = target_question.correct_answer == ans.user_answer

            if is_correct:
                score += 1

            user_answers_instances.append(
                myModels.Users_answers.objects.create(
                    score=socre_instance,
                    corect_answer=target_question.correct_answer,
                    submitted_answer=ans.user_answer,
                    is_correct=ans.user_answer == target_question.correct_answer,
                )
            )
        socre_instance.score = score
        socre_instance.save()

        return SubmitQuiz(
            score=socre_instance, submitted_answers=user_answers_instances
        )
        # return SubmitQuiz(test="test" )


class Quizzes_Mutation(graphene.ObjectType):
    create_Quiz = CreateQuiz.Field()
    create_Questions = CreateQuestions.Field()

    update_Quiz = UpdateQuiz.Field()
    update_Questions = UpdateQuestions.Field()

    delete_quiz = DeleteQuiz.Field()
    delete_question = DeleteQuestion.Field()

    submit_quiz = SubmitQuiz.Field()
