from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.is_staff


class IsOperator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_operator
