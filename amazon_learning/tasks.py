from celery import shared_task
from amazon_learning.models import Note
from datetime import datetime
import pytz
import requests
from my_amazon_learning.settings import config


@shared_task(name='test_celery_eco_system')
def sample_task():
    return {
        'success': True,
        'data': 'test_celery_eco_system is working !'
    }


@shared_task(name='dump_notes_table')
def dump_notes_table():
    aws_lambda_api_endpoint = config['LAMBDA_END_POINT']

    Note.objects.create(note=f'This is a note generated at {datetime.now(pytz.utc)} UTC')
    request = requests.post(aws_lambda_api_endpoint)
    operation_success = True if request.status_code == 200 else False

    return {'task_success': True, 'operation_success': operation_success}
