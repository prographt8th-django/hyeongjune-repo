from django.contrib import admin

from areas.models import AreaVisitStatistic, Area

admin.site.register([Area, AreaVisitStatistic])
