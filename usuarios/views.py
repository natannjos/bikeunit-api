from .models import Profile
from rest_framework import viewsets, permissions, generics
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from usuarios.serializers import ProfileSerializer
from usuarios.permissions import IsLoggedUserOrReadOnly
from django.contrib.auth import update_session_auth_hash


class ProfileViewset(viewsets.ModelViewSet):
    """API endpoint that allows profiles to be viewed or edited"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, IsLoggedUserOrReadOnly)
