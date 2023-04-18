import os

from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

CELERY_TIMEZONE = 'Asia/Seoul'

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.update(
    CELERYBEAT_SCHEDULE={
        'update_valid_areas': {
            'task': 'config.tasks.update_valid_areas',
            'schedule': '1 0 1 * *',
        },
        'update_area_visit_statistic': {
            'task': 'config.tasks.update_visit_areas',
            'schedule': '5 12 * * *'
        }
    }
)
