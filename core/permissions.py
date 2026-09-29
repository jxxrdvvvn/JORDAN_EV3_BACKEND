from rest_framework import permissions

class SoloStaffBorra(permissions.BasePermission):
    """
    Cualquier usuario autenticado puede leer, crear y editar.
    Solo los usuarios de staff (administradores) pueden eliminar registros.
    """
    def has_permission(self, request, view):
        if request.method == "DELETE":
            return request.user and request.user.is_staff
        return request.user and request.user.is_authenticated