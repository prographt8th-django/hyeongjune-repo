from django.db import models

from areas import GenderType, AgeGroupType, CompanionType


class Area(models.Model):
    code = models.CharField(max_length=31)
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class AreaVisitStatistic(models.Model):
    area = models.ForeignKey('areas.Area', on_delete=models.CASCADE)
    gender = models.CharField(max_length=31, choices=GenderType.CHOICES, default=GenderType.ALL)
    age_group = models.CharField(max_length=31, choices=AgeGroupType.CHOICES, default=AgeGroupType.TWENTY)
    companion = models.CharField(max_length=31, choices=CompanionType.CHOICES, default=CompanionType.NOT_FAMILY)
    travel_count = models.PositiveIntegerField(default=0)
    travel_date = models.DateField()

    def __str__(self):
        return f'{self.area}, {self.gender}, {self.age_group}, {self.companion}, {self.travel_date}'
