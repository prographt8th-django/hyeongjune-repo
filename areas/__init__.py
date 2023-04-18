from django.utils.translation import pgettext_lazy


class GenderType:
    ALL = 'all'
    FEMALE = 'female'
    MALE = 'male'

    CHOICES = (
        (ALL, pgettext_lazy(
            'Type of Gender',
            'all',
        )),
        (FEMALE, pgettext_lazy(
            'Type of Gender',
            'female',
        )),
        (MALE, pgettext_lazy(
            'Type of Gender',
            'male',
        )),
    )


class AgeGroupType:
    TEN = 10
    TWENTY = 20
    THIRTY = 30
    FORTY = 40
    FIFTY = 50

    CHOICES = (
        (TEN, pgettext_lazy(
            'Type of AgeGroup',
            'ten',
        )),
        (TWENTY, pgettext_lazy(
            'Type of AgeGroup',
            'twenty',
        )),
        (THIRTY, pgettext_lazy(
            'Type of AgeGroup',
            'thirty',
        )),
        (FORTY, pgettext_lazy(
            'Type of AgeGroup',
            'forty',
        )),
        (FIFTY, pgettext_lazy(
            'Type of AgeGroup',
            'fifty',
        )),
    )


class CompanionType:
    FAMILY = 'family'
    NOT_FAMILY = 'not_family'
    FAMILY_WITH_CHILD = 'family_w_child'

    CHOICES = (
        (FAMILY, pgettext_lazy(
            'Type of Companion',
            'family',
        )),
        (NOT_FAMILY, pgettext_lazy(
            'Type of Companion',
            'not_family',
        )),
        (FAMILY_WITH_CHILD, pgettext_lazy(
            'Type of Companion',
            'family_with_child',
        )),
    )
