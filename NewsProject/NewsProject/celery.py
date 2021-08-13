from __future__ import absolute_import

import os

from django.conf import settings

from celery import Celery
from celery.schedules import crontab

#Example cron: Executes every Monday morning at 7:30 A.M
#crontab(hour=7, minute=30, day_of_week=1),

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsProject.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('NewsProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_and_store_news_aapl_60s': {
        'task': 'NewsApi.tasks.get_and_store_news',
        'schedule': 60.0,
        'args': ('AAPL',)
    },
    'get_and_store_news_twtr_60s': {
        'task': 'NewsApi.tasks.get_and_store_news',
        'schedule': 60.0,
        'args': ('TWTR',)
    },
    'get_and_store_news_gcgold_60s': {
        'task': 'NewsApi.tasks.get_and_store_news',
        'schedule': 60.0,
        'args': ('GC=F(GOLD)',)
    },
    'get_and_store_news_intc_60s': {
        'task': 'NewsApi.tasks.get_and_store_news',
        'schedule': 60.0,
        'args': ('INTC',)
    },
}

app.autodiscover_tasks()
