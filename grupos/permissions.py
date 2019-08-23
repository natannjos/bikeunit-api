from rest_framework import permissions
from .models import Grupo


class IsGroupAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method == 'GET':
            return True

        # Write permissions are only allowed to the owner of the Grupo.
        return obj.admin == request.user.profile


class IsGroupAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        print(request.user.profile)
        return request.user.profile.is_grupo_admin


class IsPedalOwnerOrReadOnly(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        grupos = Grupo.objects.filter(admin=request.user.profile)

        return obj.grupo in grupos and request.user.profile.is_grupo_admin
