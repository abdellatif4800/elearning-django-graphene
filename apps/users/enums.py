import graphene
from .models import CustomUser


class RoleEnum(graphene.Enum):
    AUT = "AUT"
    ADM = "ADM"
    STU = "STU"
    INS = "INS"
    GUE = "GUE"
    REV = "REV"
