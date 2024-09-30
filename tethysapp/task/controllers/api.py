from tethys_sdk.routing import controller # type: ignore
import json
from django.http import JsonResponse # type: ignore

TASK = {
    '1': 'Task 01',
    '2': 'Task 02',
}

@controller(url='api/tasks', method='GET')
def get_task(request):
    return JsonResponse(TASK)