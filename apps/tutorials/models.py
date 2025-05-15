from django.db import models
from django.contrib.auth.models import Group, User


from pydantic import BaseModel, HttpUrl, ValidationError
from typing import List
from django.core import serializers


class Tutorial(models.Model):
    name = models.CharField(null=True)
    created_at = models.DateTimeField(null=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    members_group = models.ForeignKey(Group, to_field='name',
                                      on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class ImageSchema(BaseModel):
    urls: HttpUrl
    alt_texts: str


class Tutorial_Unit(models.Model):
    tutorial = models.ForeignKey(
        Tutorial, on_delete=models.CASCADE, related_name="units")
    title = models.CharField(default="Introduction")
    content = models.TextField()
    unit_number = models.IntegerField()
    images = models.JSONField(null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.images:
            # raises ValidationError if invalid
            try:
                validate = ImageSchema(**self.images)
                print("img", validate)
                super().save(*args, **kwargs)
            except ValidationError as e:
                print("image Validation error:")
                print(e)


# course1 = Course(
#     name='Course 1',
#     group=Group.objects.get(name="Course1 Group")
# )
# print(course1)
# target_course = Course.objects.get(name="Course 1")
# parag1 = Paragraphs(
# course=target_course,
# title="Paragraph3",
# content="Sint eiusmod nulla excepteur sint sint amet. Cupidatat fugiat Lorem et excepteur ullamco aute eu mollit ullamco esse consectetur exercitation excepteur. Est laboris cillum ea sunt amet Lorem. Eiusmod aliquip deserunt ipsum et nulla culpa deserunt dolore deserunt. Proident elit ut excepteur elit ex nulla qui labore dolor voluptate. Duis consectetur consequat voluptate do dolore consectetur veniam sint. Exercitation magna adipisicing Lorem exercitation nostrud cupidatat anim occaecat cillum.",
# paragraph_number="1",
# images={
# "urls": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fletsenhance.io%2F&psig=AOvVaw3CcAZbBKscuIL8m2wB7dLu&ust=1747293481312000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKCqhc21oo0DFQAAAAAdAAAAABAE",
#
# "urls": "sd",
# "alt_texts": "Figure 1-10"
# },
# )
# parag1.save()
# target_course.paragraphs.add(parag1)
# course1.paragraphs.add(parag1)
# course_serialized = serializers.serialize("json", [course1])
# parag1_serialized = serializers.serialize("json", [parag1])

# print("******************************************************")
# print(course_serialized)
# print(parag1_serialized)
# print("______________________________________________________")
