from .models import Profile
from rest_framework import viewsets, permissions
from usuarios.serializers import ProfileSerializer
from usuarios.permissions import IsLoggedUserOrReadOnly
from rest_framework.response import Response
from rest_framework import status


class ProfileViewset(viewsets.ModelViewSet):
    """API endpoint that allows profiles to be viewed or edited"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, IsLoggedUserOrReadOnly)

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"detail": "Você não tem permissão para executar essa ação."})
