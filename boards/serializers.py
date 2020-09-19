from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Board, Task

class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
		new_user = User(**validated_data)
		new_user.set_password(new_user.password)
		new_user.save()
		return validated_data


class BoardCreateSerializer(serializers.ModelSerializer):
	tasks = serializers.SerializerMethodField()
	class Meta:
		model = Board
		fields = ['title', 'tasks']
	
	def get_tasks(self, obj):
		return obj.tasks

class BoardListSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title']

class TaskListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ['description', 'creation_date', 'is_hidden', 'is_done']

class TaskCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ['description', 'is_hidden', 'is_done']

class TaskModifySerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ['description', 'is_hidden', 'is_done']
