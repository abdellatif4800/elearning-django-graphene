from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

from .models import Question, Quiz


def _recalc_questions_count(quiz_id: int):
    count = Question.objects.filter(quiz_id=quiz_id).count()
    Quiz.objects.filter(pk=quiz_id).update(
        questions_count=count,
    )


@receiver(post_save, sender=Question)
def question_saved(sender, instance, **kwargs):
    _recalc_questions_count(instance.quiz_id)


@receiver(post_delete, sender=Question)
def question_deleted(sender, instance, **kwargs):
    _recalc_questions_count(instance.quiz_id)
