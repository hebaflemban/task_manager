"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from boards import views as apiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', apiView.Register.as_view(), name='register'),

    path('boards/create/', apiView.BoardCreate.as_view(), name='create-board'),
    path('my-boards/', apiView.MyBoardList.as_view(), name='my-boards'),
    path('boards/', apiView.BoardList.as_view(), name='all-boards'),
    path('boards/<int:board_id>/', apiView.TaskList.as_view(), name='all-boards'),
    path('boards/<int:board_id>/delete', apiView.TaskList.as_view(), name='delete-board'),
    
    path('boards/<int:board_id>/add-task', apiView.AddTask.as_view(), name='add-task'),
    path('task/<int:task_id>/update/', apiView.ModifyTask.as_view(), name='task-update'),
    path('task/<int:task_id>/delete/', apiView.ModifyTask.as_view(), name='task-delete'),

]
