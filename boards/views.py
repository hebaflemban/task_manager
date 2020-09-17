from django.shortcuts import render
from datetime import datetime
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .models import Task, Board
#from .permissions import
from .serializers import RegisterSerializer, BoardCreateSerializer, BoardSerailizer

class Register(CreateAPIView):
    serializer_class = RegisterSerializer


class BoardCreat(CreateAPIView):
    serializer_class = BoardCreateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class MyBoardList(ListAPIView):
    serializer_class = BoardSerailizer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Board.objects.filter(owner = self.request.user )


class BoardList(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer
	permission_classes = [IsAuthenticated]
