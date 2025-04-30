from django.db import models


class CourseModel(models.Model):
    content = models.TextField()
    title = models.CharField()
