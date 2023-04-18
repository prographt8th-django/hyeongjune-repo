from django.contrib import admin

from accounts.models import User, SocialInfo

admin.site.register(User)
admin.site.register(SocialInfo)
