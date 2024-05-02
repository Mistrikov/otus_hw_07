from rest_framework import permissions


class OnlyForTeachers(permissions.BasePermission):  # можно наследоваться от IsAuthenticated
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        user = request.user
        return user.username == 'teacher1'
