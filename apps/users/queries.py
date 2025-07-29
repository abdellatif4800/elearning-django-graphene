from django.contrib.auth import authenticate, login

import graphene
import graphene_django

from . import types as myTypes
from .helper import generate_token
import logging

logger = logging.getLogger(__name__)


class usersQueries(graphene.ObjectType):
    signin = graphene.Field(
        myTypes.SigninType, username=graphene.String(), password=graphene.String()
    )

    def resolve_signin(root, info, **kwargs):
        username = kwargs["username"]
        password = kwargs["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            token = generate_token(
                {"username": username, "user_id": user.id, "is_staff": user.is_staff}
            )

            return myTypes.SigninType(token=token)
