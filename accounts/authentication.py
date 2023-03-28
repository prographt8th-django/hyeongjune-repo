import jwt
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from accounts.jwt import decode_jwt
from accounts.models import User


class JSONWebTokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        headers = request.headers
        jwt_value = headers.get("Authorization", None)
        if jwt_value is None:
            return None
        try:
            payload = decode_jwt(jwt_value)

        except jwt.ExpiredSignature:
            msg = 'Signature has expired.'
            raise exceptions.AuthenticationFailed(msg)

        except jwt.DecodeError:
            msg = 'Error decoding signature.'
            raise exceptions.AuthenticationFailed(msg)

        except jwt.InvalidTokenError:
            msg = 'Invalid Token'
            raise exceptions.AuthenticationFailed(msg)

        user_id = payload.get('user_id', '')
        user = User.objects.filter(user_id=user_id)
        if not user:
            msg = 'Invalid Token'
            raise exceptions.AuthenticationFailed(msg)
        return user, None
