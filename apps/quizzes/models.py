from django.db import models
from django.contrib.auth.models import Group
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Quiz(models.Model):
    name = models.CharField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    category = models.CharField(null=False)
    questions_count = models.IntegerField()
    published = models.BooleanField(null=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk and Quiz.objects.filter(pk=self.pk).exists():
            # Only update when it's not creation
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class Question(models.Model):
    MULTIPLE_CHOICE = "MC"
    TRUE_FALSE = "TF"
    SHORT_ANSWER = "SA"

    QUESTION_TYPES = [
        (MULTIPLE_CHOICE, "Multiple Choice"),
        (TRUE_FALSE, "True/False"),
        (SHORT_ANSWER, "Short Answer"),
    ]
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="questions", null=False
    )
    question = models.TextField(null=False)
    correct_answer = models.TextField(null=False)
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPES, null=False)


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers", null=False
    )
    answer = models.TextField(null=False)


class Score(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="quiz_scores", null=False
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_scores", null=False
    )
    score = models.IntegerField(null=False)
    submitted_at = models.DateTimeField(default=timezone.now)


class Users_answers(models.Model):
    score = models.ForeignKey(
        Score, on_delete=models.CASCADE, related_name="submitted_answers"
    )
    corect_answer = models.CharField(null=False)
    submitted_answer = models.CharField(null=False)
    is_correct = models.BooleanField(null=False)
