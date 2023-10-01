from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from task.models import Task
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .permissions import IsOwnerPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.filter(is_done=False)

    # def get_queryset(self,*args, **kwargs):

    #     return (
    #         super()
    #         .get_queryset(*args, **kwargs)
    #         .filter(user = self.request.user)
    #     )

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {"author": ["exact", "in"]}
    search_fields = ["title"]
    ordering_fields = ["datetime_created"]
    pagination_class = DefaultPagination
