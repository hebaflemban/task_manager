from django.shortcuts import render
from datetime import datetime
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from .models import Task, Board

from .serializers import RegisterSerializer, BoardCreateSerializer, BoardListSerailizer, TaskCreateSerializer, TaskListSerializer, TaskModifySerializer
from .permissions import IsOwner, IsBoardOwner

class Register(CreateAPIView):
    serializer_class = RegisterSerializer


class BoardCreate(CreateAPIView):
    serializer_class = BoardCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MyBoardList(ListAPIView):
    serializer_class = BoardListSerailizer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Board.objects.filter(owner = self.request.user )


class BoardList(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer
    permission_classes = [IsAuthenticated]

class TaskList(ListAPIView):
    serializer_class = TaskListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'board_id'
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['creation_date', 'is_hidden', 'is_done']


    def get_queryset(self):
        board_obj = Board.objects.get(id=self.kwargs['board_id'])
        if self.request.user == board_obj.owner:
            tasks = Task.objects.filter(board=board_obj)
            return TaskListSerializer(tasks, many=True).data
        tasks = Task.objects.filter(board=board_obj, is_hidden=0)
        return TaskListSerializer(tasks, many=True).data


class AddTask(CreateAPIView):
    serializer_class = TaskCreateSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(board_id=self.kwargs['board_id'])

class ModifyTask(RetrieveUpdateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskModifySerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'task_id'	
	permission_classes = [IsAuthenticated, IsBoardOwner]

class DeleteBoard(DestroyAPIView):
    queryset = Board.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'board_id'
    permission_classes = [IsAuthenticated, IsOwner]

class DeleteTask(DestroyAPIView):
    queryset = Task.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'task_id'
    permission_classes = [IsAuthenticated, IsBoardOwner]
