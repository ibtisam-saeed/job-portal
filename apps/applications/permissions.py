from rest_framework.permissions import BasePermission


class CanCreateApplication(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.has_perm('applications.can_create_application')
        )