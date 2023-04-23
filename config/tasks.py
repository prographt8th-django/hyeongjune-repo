import requests
from celery import shared_task
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from areas import GenderType, AgeGroupType, CompanionType
from areas.models import Area, AreaVisitStatistic

from datetime import datetime

from config.utils import export_celery_log

valid_area_search_url = 'https://apis.openapi.sk.com/puzzle/travel?type=sig'
area_visit_statistic_url = 'https://apis.openapi.sk.com/puzzle/traveler-count/raw/daily/districts/'
target_areas = ['1111000000', '1117000000', '1171000000']
headers = {
    'appkey': settings.SK_API_APP_KEY,
    'content-type': 'application/json'
}


@shared_task
def update_valid_areas():
    response = requests.get(valid_area_search_url, headers=headers)
    valid_areas = response.json().get('contents')
    for area in valid_areas:
        try:
            area = Area.objects.get(code=area['districtCode'])
        except ObjectDoesNotExist:
            Area.objects.create(code=area['districtCode'],
                                name=area['districtName'])
    export_celery_log('celery_logs', str(valid_areas))


@shared_task
def update_visit_areas():
    try:
        for target in target_areas:
            for gender in GenderType.CHOICES:
                for age_group in AgeGroupType.CHOICES:
                    for companion_type in CompanionType.CHOICES:
                        params = {'gender': gender[0], 'ageGrp': age_group[0], 'companionType': companion_type[0]}
                        response = requests.get(area_visit_statistic_url + target, headers=headers, params=params)
                        valid_statistics = response.json()['contents']['raw']
                        date = datetime.strptime(valid_statistics[-1]['date'], '%Y%m%d').date()
                        area = Area.objects.get(code=target)
                        AreaVisitStatistic.objects.create(area=area, gender=gender[0], age_group=age_group[0],
                                                          companion=companion_type[0],
                                                          travel_count=valid_statistics[-1]['travelerCount'] or 0,
                                                          travel_date=date)
                        export_celery_log('celery_logs', str(valid_statistics[-1]))
    except Exception as e:
        print(e)
