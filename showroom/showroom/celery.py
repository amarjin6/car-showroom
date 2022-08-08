import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'showroom.settings')
app = Celery('showroom')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'buy-car-every-10-minute': {
        'task': 'orders.tasks.buy_car',
        'schedule': crontab(minute='*/10'),  # minute=0, hour='*/1' # add bool field to return
    },
}
