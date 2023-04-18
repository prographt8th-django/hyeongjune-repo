from django.db import models


class Subway(models.Model):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=31)
    line = models.ForeignKey('subways.SubwayLine', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class SubwayLine(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
