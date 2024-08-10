from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Класс для проверки принадлежности продукта владельцу"""

    message = "Доступно владельцу"

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False