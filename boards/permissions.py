from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
	message = "You must be the owner of this item"

	def has_object_permission(self, request, view, obj):
		if (obj.owner == request.user):
			return True
		else:
			return False

class IsBoardOwner(BasePermission):
	message = "You must be the owner of this item"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.board.owner == request.user):
			return True
		else:
			return False
