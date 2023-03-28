from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'nickname',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
