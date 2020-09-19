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
    path('boards/<int:board_id>/', apiView.TaskList.as_view(), name='board'),
    path('boards/<int:board_id>/delete', apiView.TaskList.as_view(), name='delete-board'),

    path('boards/<int:board_id>/add-task', apiView.AddTask.as_view(), name='add-task'),
    path('task/<int:task_id>/update/', apiView.ModifyTask.as_view(), name='task-update'),
    path('task/<int:task_id>/delete/', apiView.ModifyTask.as_view(), name='task-delete'),

]
