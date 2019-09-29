from .models import Pedal, Grupo
from rest_framework import viewsets, permissions
from grupos.serializers import GrupoSerializer, PedalSerializer, PedalReadOnlylSerializer, GrupoReadOnlySerializer, EntrarESairDePedalSerializer
from grupos.permissions import IsGroupAdminOrReadOnly, IsGroupAdmin, IsPedalOwnerOrReadOnly, CannotCreateOrDelete
from rest_framework.response import Response
from rest_framework import status


class TodosGruposViewset(viewsets.ModelViewSet):
    """API endpoint that allows grupos to be viewed or edited"""

    queryset = Grupo.objects.all()
    serializer_class = GrupoReadOnlySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsGroupAdminOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user.profile)

    def create(self, request):
        user = request.user.profile

        if user.is_grupo_admin:
            return super(TodosGruposViewset, self).create(request)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"detail": "Você não tem permissão para executar essa ação."})


class MeusGruposViewset(viewsets.ModelViewSet):
    serializer_class = GrupoSerializer
    queryset = Grupo.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
        IsGroupAdmin, )

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(admin=self.request.user.profile)
        return query_set

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user.profile)

    def create(self, request):
        user = request.user.profile

        if user.is_grupo_admin:
            return super(MeusGruposViewset, self).create(request)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"detail": "Você não tem permissão para executar essa ação."})


class TodosPedaisViewset(viewsets.ModelViewSet):
    """API endpoint that allows pedais to be viewed or edited"""
    serializer_class = PedalReadOnlylSerializer
    queryset = Pedal.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsPedalOwnerOrReadOnly
    )

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
        permissions.IsAuthenticatedOrReadOnly,
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


class EntrarESairDePedalViewset(viewsets.ModelViewSet):
    serializer_class = EntrarESairDePedalSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        CannotCreateOrDelete,
    )
    queryset = Pedal.objects.all()

    def partial_update(self, request, pk=None):
        serialized = EntrarESairDePedalSerializer(
            request.user, data=request.data, partial=True)
        print('Serialized: ', serialized)
        return Response(status=status.HTTP_202_ACCEPTED)
