from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from task.models import Task
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

"""
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
"""

"""
@api_view(['GET','PUT','DELETE'])
def task_detail(request,pk):
    task = get_object_or_404(Task,id=pk,is_done=False)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(task,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        task.delete()
        return Response({'detail':'task has been removed'})
"""


class TaskList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        tasks = Task.objects.filter(is_done=False)
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class TaskDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        task = get_object_or_404(Task,id=pk,is_done=False)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self,request,pk):
        task = get_object_or_404(Task,id=pk,is_done=False)
        serializer = TaskSerializer(task,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        task = get_object_or_404(Task,id=pk,is_done=False)
        task.delete()
        return Response({'detail':'task has been removed'})