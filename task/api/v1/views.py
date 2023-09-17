from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from task.models import Task


@api_view(['GET','POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(is_done=False)
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    else:
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    