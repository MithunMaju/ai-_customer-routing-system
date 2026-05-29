from celery import shared_task
from requestscust.models import CustomerRequest
from classification.models import Classification
from .ai import classify_message


@shared_task
def classify_request(request_id):
    request = CustomerRequest.objects.get(
        id=request_id
    )
    result = classify_message(
        request.message
    )
    Classification.objects.create(
        request=request,
        category=result['category'],
        priority=result['priority'],
    )
    request.status = 'in_progress'
    request.save()