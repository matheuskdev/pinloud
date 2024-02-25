from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners or admin to edit/delete an object.
    """
    def has_object_permission(self, request, view, obj):
        # Permite a leitura (GET, HEAD ou OPTIONS) para qualquer solicitação.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permite a edição ou exclusão apenas se o usuário for o dono ou admin.
        return obj.user == request.user or request.user.is_staff
