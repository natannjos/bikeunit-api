from .models import Profile
from rest_framework import viewsets, permissions, generics
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from usuarios.serializers import ProfileSerializer, ChangePasswordSerializer
from usuarios.permissions import IsLoggedUserOrReadOnly
from django.contrib.auth import update_session_auth_hash


class ProfileViewset(viewsets.ModelViewSet):
    """API endpoint that allows profiles to be viewed or edited"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsLoggedUserOrReadOnly, )


class ChangePasswordView(generics.UpdateAPIView):
    """API endpoint for changing password"""

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated, IsLoggedUserOrReadOnly)

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Senha inválida."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            update_session_auth_hash(request, self.object)

            return Response("Senha Alterada com Sucesso.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
