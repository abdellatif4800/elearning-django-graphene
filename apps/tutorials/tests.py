import json
from graphene_django.utils.testing import GraphQLTestCase
from . import models
from pprint import pprint


class Create_tutorial(GraphQLTestCase):
    GRAPHQL_URL = "/graphql/"

    # def setUp(self):
    #     # Create a tutorial object in the test database
    #     self.tutorial = Tutorial.objects.create(
    #         id=103,
    #         name="Test Tutorial"
    #     )

    def test_new_tutorial(self):
        response = self.query(
            """
            mutation CreateTutorial {
                createTutorial(tutorialData: { author: "11", name: "TUT102" }) {
                    tutorial {
                        id
                        name
                        createdAt
                        updatedAt
                    }
                }
            }


            """
            # ,
            # op_name="GetTutorial"
        )
        content = json.loads(response.content)
        print("*******************************")
        print("Status Code:", response.status_code)
        print("Response Content:", content)
        print("-------------------------------")

        self.assertResponseNoErrors(response)


class Retrive_Tutorial(GraphQLTestCase):
    GRAPHQL_URL = "/graphql/"

    def setUp(self):
        models.Tutorial.objects.bulk_create(
            [
                models.Tutorial(
                    id=101,
                    name="Test Tutorial1"
                ), models.Tutorial(
                    id=102,
                    name="Test Tutorial12"
                ), models.Tutorial(
                    id=103,
                    name="Test Tutorial13"
                )
            ]
        )

        models.Tutorial_Unit.objects.bulk_create(
            [
                # tut 101
                models.Tutorial_Unit(
                    tutorial=models.Tutorial.objects.get(id=101),
                    title="Test Unit1",
                    content="Culpa in ut et pariatur laboris ipsum ea magna proident adipisicing est commodo.",
                    unit_number=1,
                    images="https://example.com/image1.jpg"

                ),
                models.Tutorial_Unit(
                    tutorial=models.Tutorial.objects.get(id=101),
                    title="Test Unit2",
                    content="Culpa in ut et pariatur laboris ipsum ea magna proident adipisicing est commodo.",
                    unit_number=2,
                    images="https://example.com/image1.jpg"

                ), models.Tutorial_Unit(
                    tutorial=models.Tutorial.objects.get(id=101),
                    title="Test Unit3",
                    content="Culpa in ut et pariatur laboris ipsum ea magna proident adipisicing est commodo.",
                    unit_number=3,
                    images="https://example.com/image1.jpg"

                ),


                # tut 102
                models.Tutorial_Unit(
                    tutorial=models.Tutorial.objects.get(id=102),
                    title="Test Unit1",
                    content="Culpa in ut et pariatur laboris ipsum ea magna proident adipisicing est commodo.",
                    unit_number=1,
                    images="https://example.com/image1.jpg"

                ),
                models.Tutorial_Unit(
                    tutorial=models.Tutorial.objects.get(id=102),
                    title="Test Unit2",
                    content="Culpa in ut et pariatur laboris ipsum ea magna proident adipisicing est commodo.",
                    unit_number=2,
                    images="https://example.com/image1.jpg"

                ), models.Tutorial_Unit(
                    tutorial=models.Tutorial.objects.get(id=102),
                    title="Test Unit3",
                    content="Culpa in ut et pariatur laboris ipsum ea magna proident adipisicing est commodo.",
                    unit_number=3,
                    images="https://example.com/image1.jpg"

                ),

            ]

        )

    def test_list_tutorial_units(self):
        response = self.query(
            """
            query ListTutorialsUnits {
                listUnitsPerTutorial(tutorialId:102) {
                   title
                    id
                    tutorial {
                        name
                        id
                    }
                }
            }
            """
            # ,
            # op_name="GetTutorial"
        )
        content = json.loads(response.content)
        print("*************Retrive_Tutorial******************")
        print("Response Content:")
        pprint(content)
        print("-------------------------------")
        self.assertResponseNoErrors(response)

    def test_list_tutorial(self):
        response = self.query(
            """
            query ListTutorials {
                listTutorial {
                    id
                    name
                }
            }
            """
            # ,
            # op_name="GetTutorial"
        )
        content = json.loads(response.content)
        print("*************Retrive_Tutorial******************")
        print("Response Content:")
        pprint(content)
        print("-------------------------------")
        self.assertResponseNoErrors(response)

    def test_retrive_tutorial(self):
        response = self.query(
            """
            query GetTutorial {
                getTutorial(id: 103) {
                    id
                    name
                    createdAt
                    updatedAt
                }
            }
            """
            # ,
            # op_name="GetTutorial"
        )
        content = json.loads(response.content)
        print("*************Retrive_Tutorial******************")
        print("Response Content:")
        pprint(content)
        print("-------------------------------")
        self.assertResponseNoErrors(response)

    def test_retrive_tutoril_unit(self):
        response = self.query(
            """
            mutation CreateUnit($data: UnitInput) {
                createUnit(unitData: $data) {
                    unit {
                    content
                    id
                    images
                    title
                    unitNumber
                    tutorial {
                        name
                        id
                    }
                    }
                }
            }
            """,
            variables={
                "data": {
                    "tutorial": f"{self.tutorial.id}",
                    "title": "Title 2",
                    "content": "Culpa in ut et pariatur laboris ipsum ea magna proident adipisicing est commodo. ",
                    "unitNumber": 3,
                    "images": "https://example.com/image1.jpg"
                }
            }
        )
        content = json.loads(response.content)
        print("*************Retrive_Tutorial_unit******************")
        print("Status Code:", response.status_code)
        print("Response Content:")
        pprint(content)
        print("-------------------------------")
        self.assertResponseNoErrors(response)
