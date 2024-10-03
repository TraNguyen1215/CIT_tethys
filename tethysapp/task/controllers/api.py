from tethys_sdk.routing import controller
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

TASK = {
    '1': 'Task 01',
    '2': 'Task 02',
}

@controller(url='api/tasks/', method='GET')
@csrf_exempt
def get_tasks(request):
    return JsonResponse(TASK, safe=False)
    # for task_id, task_name in TASK.items():
    #     # Kiểm tra xem ID đã tồn tại trong TASK chưa
    #     if task_id in TASK:
    #         TASK[str(task_id)] = 'Hi'
    #         return JsonResponse(TASK[str(task_id)], safe=False)  # Trả về task nếu có ID


@controller(url='/apps/task/api/tasks/', method='POST')
@csrf_exempt
def add_task(request):
    # Tải nội dung JSON từ request.body
    data = json.loads(request.body)
    
    # Giả định rằng data là một từ điển với id là key và tên task là value
    for task_id, task_name in data.items():
        TASK[str(task_id)] = task_name
    
    # Trả về phản hồi JSON
    return JsonResponse(TASK[str(task_id)], safe=False)

@controller(url='/apps/task/api/tasks/', method='PUT')
@csrf_exempt
def update_task(request):
    data = json.loads(request.body)
    for task_id, task_name in data.items():
        # Kiểm tra xem ID có tồn tại trong TASK không
        if task_id not in TASK:
            return JsonResponse({'error': f'Task with ID {task_id} not found.'}, status=404)
        # Cập nhật task
        TASK[str(task_id)] = task_name
    
    # Trả về phản hồi JSON
    return JsonResponse(data, safe=False)

@controller(url='/apps/task/api/tasks/', method='DELETE')
@csrf_exempt
def delete_task(request, task_id):
    # Kiểm tra xem ID có tồn tại trong TASK không
    if task_id not in TASK:
        return JsonResponse({'error': f'Task with ID {task_id} not found.'}, status=404)
    
    # Xóa task
    del TASK[task_id]
    
    # Trả về phản hồi JSON
    return JsonResponse({'success': f'Task with ID {task_id} deleted.'})
    

