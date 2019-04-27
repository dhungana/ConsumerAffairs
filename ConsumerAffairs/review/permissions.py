from rest_framework import permissions

class IsOwner(permissions.BasePermission):
	message = "Permission Denied: You do not have proper authority."

	def has_obj_permission(self, request, view, obj):
		if obj.reviewer == request.user:
			return True
		return False
