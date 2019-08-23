from .models import Pedal, Grupo
from rest_framework import viewsets, permissions
from grupos.serializers import GrupoSerializer, PedalSerializer, PedalReadOnlylSerializer, GrupoReadOnlySerializer
from grupos.permissions import IsGroupAdminOrReadOnly, IsGroupAdmin, IsPedalOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status


class TodosGruposViewset(viewsets.ModelViewSet):
    """API endpoint that allows grupos to be viewed or edited"""

    queryset = Grupo.objects.all()
    serializer_class = GrupoReadOnlySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsGroupAdminOrReadOnly)

    def create(self, request):
        if not request.user.profile.is_grupo_admin:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"detail": "Você não tem permissão para executar essa ação."})
        return super(TodosGruposViewset, self).create(request)


class MeusGruposViewset(viewsets.ModelViewSet):
    serializer_class = GrupoSerializer
    queryset = Grupo.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
        IsGroupAdmin, )

    def create(self, request):
        if request.user.profile.is_grupo_admin:
            return super(MeusGruposViewset, self).create(request)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"detail": "Você não tem permissão para executar essa ação."})

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(admin=self.request.user.profile)
        return query_set


class TodosPedaisViewset(viewsets.ModelViewSet):
    """API endpoint that allows pedais to be viewed or edited"""

    queryset = Pedal.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsPedalOwnerOrReadOnly
    )

    def get_serializer_class(self):
        user = self.request.user.profile
       # usuario_admin_grupos = Grupo.objects.filter(admin=user)
        # print(self.get_object())
        # if self.get_object().grupo in usuario_admin_grupos:
        #    return PedalSerializer
        return PedalReadOnlylSerializer

    def create(self, request):
        user_grupos = Grupo.objects.filter(admin=request.user.profile)
        id = request.data['grupo']
        request_grupo = Grupo.objects.get(id=id)
        if request.user.profile.is_grupo_admin and request_grupo in user_grupos:
            return super(TodosPedaisViewset, self).create(request)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"detail": "Você não tem permissão para executar essa ação."})


class MeusPedaisViewset(viewsets.ModelViewSet):
    serializer_class = PedalSerializer
    queryset = Pedal.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
        IsPedalOwnerOrReadOnly, )

    def create(self, request):
        user_grupos = Grupo.objects.filter(admin=request.user.profile)
        id = request.data['grupo'].split('/')[-2]
        request_grupo = Grupo.objects.get(id=id)
        if request.user.profile.is_grupo_admin and request_grupo in user_grupos:
            return super(MeusPedaisViewset, self).create(request)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"detail": "Você não tem permissão para executar essa ação."})

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(grupo__admin=self.request.user.profile)
        return query_set
