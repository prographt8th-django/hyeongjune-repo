from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from accounts import SocialType


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, password=None, **kwargs):

        if not email:
            raise ValueError('must have user email')
        if not nickname:
            raise ValueError('must have user nickname')

        user = self.model(
            email=email,
            nickname=nickname,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password, **kwargs):

        user = self.create_user(
            email=email,
            nickname=nickname,
            password=password,
            **kwargs,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    social_info = models.OneToOneField('accounts.SocialInfo', on_delete=models.CASCADE, related_name='user', null=True)
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.nickname

    @property
    def is_staff(self):
        return self.is_admin


class SocialInfo(models.Model):
    type = models.CharField(max_length=15, choices=SocialType.CHOICES)
    auth_id = models.CharField(max_length=63, unique=True)
