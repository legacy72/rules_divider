from rest_framework import permissions


class BookPermission(permissions.BasePermission):
    """
    Custom Permission for check user's ticket_sale group
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='books')


class FilmPermission(permissions.BasePermission):
    """
    Custom Permission for check user's ticket_sale group
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='films')


class MusicPermission(permissions.BasePermission):
    """
    Custom Permission for check user's ticket_sale group
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='musics')
