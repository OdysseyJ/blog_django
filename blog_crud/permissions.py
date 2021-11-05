from rest_framework import permissions


class IsWriterOrReadOnly(permissions.BasePermission):
    """
    Custom permission update/delete only to writer
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.writer == request.user
