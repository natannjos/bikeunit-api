from .models import Pedal, Grupo
from rest_framework import viewsets, permissions
from grupos.serializers import GrupoSerializer, PedalSerializer
from grupos.permissions import IsAdminOrReadOnly


class GrupoViewset(viewsets.ModelViewSet):
    """API endpoint that allows grupos to be viewed or edited"""

    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAdminOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)


class PedalViewset(viewsets.ModelViewSet):
    """API endpoint that allows pedais to be viewed or edited"""

    queryset = Pedal.objects.all()
    serializer_class = PedalSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAdminOrReadOnly, )
