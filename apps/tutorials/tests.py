from django.test import TestCase
from apps.tutorials.models import Tutorial
from django.contrib.auth.models import Group


class Try(TestCase):
    def test_1(self):

        tryOne = Tutorial.objects.create(
            name="Test Tutorial",
            created_at="2023-10-01T00:00:00Z",
        )
        print("****************")
        print("tryOne", tryOne)
        print("_______________")

        self.assertIsInstance(tryOne, Tutorial)
