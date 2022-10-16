import strawberry
from . import models


@strawberry.django.type(models.User)
class UserType:
    name: str
    email: str
    username: str
