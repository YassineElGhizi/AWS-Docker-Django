import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_amazon_learning.settings')
app = Celery('my_amazon_learning')

app.config_from_object('django.conf:settings', namespace="CELERY")
from django.conf import settings

# PS: VERY IMPORTAT : the task file must be names tasks.py not task.py
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
