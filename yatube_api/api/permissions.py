from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Безопасные методы разрешены всем
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Изменение и удаление разрешены только автору
        return obj.author == request.user
