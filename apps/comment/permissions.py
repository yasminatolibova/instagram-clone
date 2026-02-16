from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        

        if hasattr(obj, 'user'):
            return obj.user == request.user
        
        return obj == request.user
    

    