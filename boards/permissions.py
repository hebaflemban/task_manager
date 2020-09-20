from rest_framework.permissions import BasePermission
from .models import Board


class IsOwner(BasePermission):
	message = "You must be the owner of this board"

	def has_permission(self, request, view):
		board = Board.objects.get(id = view.kwargs['board_id'])
		if ( board.owner == request.user):
			return True
		else:
			return False

class IsBoardOwner(BasePermission):
	message = "You must be the owner of this board"

	def has_object_permission(self, request, view, obj):
		print("here1")

		if (obj.board.owner == request.user):
			return True
		else:
			return False
