from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.core.exceptions import PermissionDenied
from django.db.models import Q

# Permite apenas que coordenadores façam GET/POST/PUT/DELETE
# class DeadlineCustomPermission(BasePermission):
#     def has_permission(self,request,view):
#         return request.user.groups.filter(name='Coordenador').exists()

# CONDIÇÃO POR GRUPO
# Permite que apenas coordenadores façam POST/PUT/DELETE
# Mas permite o GET para todos os usuarios Autenticados.
# class DeadlineCustomPermission(BasePermission):
#     def has_permission(self,request,view):
#         if request.method == 'GET':
#             return request.user.is_authenticated
#         return request.user.groups.filter(Q(name='Coordenador') | Q(name='Admin')).exists()


# CONDIÇÃO POR PERMISSÃO
# Todos que tiverem a premissão view podem fazer GET
# os que tiverem permissão add, delete, change deadline podem fazer GET/POST/PUT/DELETE
class DeadlineCustomPermission(BasePermission):
    def has_permission(self,request,view):
        if request.method == 'GET':
            return request.has_perm('main.view_deadline')

        return request.has_perm('main.add_deadline','main.delete_deadline','main.change_deadline')

class DeadlineView(ModelViewSet):
    queryset = Deadline.objects.all()
    serializer_class = DeadlineSerializer
    permission_classes = (DeadlineCustomPermission,)
