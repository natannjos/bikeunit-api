from .models import Pedal, Grupo
from rest_framework import viewsets, permissions
from grupos.serializers import GrupoSerializer, PedalSerializer
from grupos.permissions import IsGroupAdminOrReadOnly
from rest_framework.response import Response
from rest_framework import status


class GrupoViewset(viewsets.ModelViewSet):
    """API endpoint that allows grupos to be viewed or edited"""

    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsGroupAdminOrReadOnly, )

    def create(self, request):
        if not request.user.profile.is_grupo_admin:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"erro": "Método não permitido"})
        return super(GrupoViewset, self).create(request)

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user.profile)


class PedalViewset(viewsets.ModelViewSet):
    """API endpoint that allows pedais to be viewed or edited"""

    queryset = Pedal.objects.all()
    serializer_class = PedalSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsGroupAdminOrReadOnly, )
