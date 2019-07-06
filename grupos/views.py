from .models import Pedal, Grupo
from rest_framework import viewsets
from grupos.serializers import GrupoSerializer, PedalSerializer


class GrupoViewset(viewsets.ModelViewSet):
    """API endpoint that allows grupos to be viewed or edited"""

    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer


class PedalViewset(viewsets.ModelViewSet):
    """API endpoint that allows pedais to be viewed or edited"""

    queryset = Pedal.objects.all()
    serializer_class = PedalSerializer
