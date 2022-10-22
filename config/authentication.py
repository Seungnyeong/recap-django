import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from users.models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Jwt")
        if not token:
            raise AuthenticationFailed("Invalid Token")
        decoded = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"],
        )
        pk = decoded.get("pk")
        if not pk:
            return None
        try:
            user = User.objects.get(pk=pk)
            return (user, None)
        except User.DoesNotExist:
            AuthenticationFailed(f"User Not Found")
