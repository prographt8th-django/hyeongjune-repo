from rest_framework import status
from rest_framework.permissions import SAFE_METHODS
from .models import User
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from .jwt import decode_jwt


class JsonWebTokenMiddleWare(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            if (
                request.path != "/api/users/kakao"
                and request.path != "/api/users/check-nickname"
                and request.path != "/api/users/google"
                and request.path != "/api/users/naver"
                and "admin" not in request.path
                and "swagger" not in request.path
                and request.method not in SAFE_METHODS
            ):
                headers = request.headers
                access_token = headers.get("Authorization", None)
                if not access_token:
                    raise PermissionDenied()

                payload = decode_jwt(access_token)
                user_id = payload.get("user_id", None)

                if not user_id:
                    raise PermissionDenied()
                user = User.objects.filter(social_id=user_id)
                if not user:
                    raise PermissionDenied()
            response = self.get_response(request)

            return response

        except (PermissionDenied, User.DoesNotExist):
            return JsonResponse(
                {"error": "Authorization Error"}, status=status.HTTP_401_UNAUTHORIZED
            )
