import requests
from rest_framework import status, mixins
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.views.generic import ListView, CreateView, UpdateView
from accounts import SocialType
from accounts.models import User
from accounts.serializers import UserSerializer
from accounts.utils import process_for_social_login


@api_view(["GET"])
def ping(request):
    res = {
        "server": "on"
    }
    return Response(res, status=status.HTTP_200_OK)


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    @action(methods=['get'], detail=False)
    def check_nickname(self, request):
        nickname = request.query_params.get('nickname', None)
        if nickname:
            _nickname = User.objects.filter(nickname=nickname)
            if _nickname:
                return Response({'message': 'duplicate nickname exists.'}, status=status.HTTP_409_CONFLICT)
            else:
                return Response({'message': 'this nickname is an available nickname.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'nickname is missing.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False)
    def kakao(self, request):
        access_token = request.data.get('access_token', None)

        if not access_token:
            return Response({'message': 'access_token is missing'}, status=status.HTTP_400_BAD_REQUEST)

        user_req = requests.get("https://kapi.kakao.com/v2/user/me",
                                headers={"Authorization": f"Bearer {access_token}"})
        user_res = user_req.json()
        result, response_data = process_for_social_login(SocialType.KAKAO, user_res)
        if not result:
            return Response({'message': 'invalid social access_token'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(response_data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def google(self, request):
        access_token = request.data.get('access_token', None)

        if not access_token:
            return Response({'message': 'access_token is missing'}, status=status.HTTP_400_BAD_REQUEST)

        social_req = requests.get(f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")
        social_res = social_req.json()
        result, response_data = process_for_social_login(SocialType.GOOGLE, social_res)
        if not result:
            return Response({'message': 'invalid social access_token'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(response_data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def naver(self, request):
        access_token = request.data.get('access_token', None)

        if not access_token:
            return Response({'message': 'access_token is missing'}, status=status.HTTP_400_BAD_REQUEST)

        social_req = requests.get("https://openapi.naver.com/v1/nid/me",
                                  headers={"Authorization": f"Bearer {access_token}"})
        social_res = social_req.json()
        result, response_data = process_for_social_login(SocialType.GOOGLE, social_res)
        if not result:
            return Response({'message': 'invalid social access_token'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(response_data, status=status.HTTP_200_OK)

