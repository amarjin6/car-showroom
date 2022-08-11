import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'showroom.settings')
app = Celery('showroom')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'process-customer-order-every-10-minute': {
        'task': 'orders.services.process_customer_order',
        'schedule': crontab(minute='*/10'),
    },
    'process-dealer-order-every-1-hour': {
        'task': 'orders.services.process_dealer_order',
        'schedule': crontab(hour='*/1'),
    },
}
