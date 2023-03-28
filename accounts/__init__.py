from django.utils.translation import pgettext_lazy


class SocialType:
    KAKAO = 'kakao'
    GOOGLE = 'google'
    NAVER = 'naver'

    CHOICES = (
        (KAKAO, pgettext_lazy(
            'Type of Social Login',
            'kakao',
        )),
        (GOOGLE, pgettext_lazy(
            'Type of Social Login',
            'google',
        )),
        (NAVER, pgettext_lazy(
            'Type of Social Login',
            'naver',
        )),
    )
