from rest_framework.permissions import BasePermission


class OwnerOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.post_owner == request.user
