from django.db import models


class Question(models.Model):
    ques = models.TextField()
    ques_type = models.CharField()
