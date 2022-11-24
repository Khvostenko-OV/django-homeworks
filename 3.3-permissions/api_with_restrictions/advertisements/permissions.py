from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    """Разрешение на изменение и удаление объявлений"""

    def has_object_permission(self, request, view, obj):
        return (request.user == obj.creator) or request.user.is_superuser