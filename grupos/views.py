from .models import Pedal, Grupo
from rest_framework import viewsets, permissions
from grupos.serializers import GrupoSerializer, PedalSerializer
from grupos.permissions import IsGroupAdminOrReadOnly, IsGroupAdmin, IsPedalOwner
from rest_framework.response import Response
from rest_framework import status


class TodosGruposViewset(viewsets.ModelViewSet):
    """API endpoint that allows grupos to be viewed or edited"""

    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsGroupAdminOrReadOnly, )

    def create(self, request):
        if not request.user.profile.is_grupo_admin:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"erro": "Método não permitido"})
        return super(TodosGruposViewset, self).create(request)

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user.profile)


class PedalViewset(viewsets.ModelViewSet):
    """API endpoint that allows pedais to be viewed or edited"""

    queryset = Pedal.objects.all()
    serializer_class = PedalSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsPedalOwner
    )

    def create(self, request):
        user_grupos = Grupo.objects.filter(admin=request.user.profile)
        id = request.data['grupo'].split('/')[-2]
        request_grupo = Grupo.objects.get(id=id)
        if request.user.profile.is_grupo_admin and request_grupo in user_grupos:
            return super(PedalViewset, self).create(request)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"erro": "Método não permitido"})


class MeusGruposViewset(viewsets.ModelViewSet):
    serializer_class = GrupoSerializer
    queryset = Grupo.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
        IsGroupAdmin, )

    def create(self, request):
        if not request.user.profile.is_grupo_admin:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"erro": "Método não permitido"})
        return super(MeusGruposViewset, self).create(request)

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(admin=self.request.user.profile)
        return query_set
