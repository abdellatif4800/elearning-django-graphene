from graphql import GraphQLError
import os
from dotenv import load_dotenv
import jwt
import logging

logger = logging.getLogger(__name__)


load_dotenv()

jwt_secret = os.getenv("JWT_SECRET")


def generate_token(payload):
    encoded = jwt.encode(payload, jwt_secret, algorithm="HS256")
    return encoded


def verify_token(func):
    def wrapper(root, info, **kwargs):
        auth_header = info.context.headers.get("Authorization")

        if auth_header is None:
            raise GraphQLError("Authentication required")

        if auth_header is not None:
            token = auth_header.split(" ")[1]
            try:
                jwt.decode(token, jwt_secret, algorithms=["HS256"])
            except jwt.InvalidTokenError:
                raise GraphQLError("Invalid token")
            except jwt.ExpiredSignatureError:
                raise GraphQLError("Token has expired")

        return func(root, info, **kwargs)

    return wrapper


def verify_admin(func):
    def wrapper(root, info, **kwargs):
        auth_header = info.context.headers.get("Authorization")
        token = auth_header.split(" ")[1]
        decoded = jwt.decode(token, jwt_secret, algorithms=["HS256"])
        if decoded.get("is_staff") == False:
            raise GraphQLError("not admin")
        else:
            kwargs["decoded_token"] = decoded
        return func(root, info, **kwargs)

    return wrapper
