from .models import Profile
from rest_framework import viewsets, permissions, generics
from rest_framework import views
#from django.contrib.auth.models import User
from core_auth.models import User
from usuarios.serializers import ProfileSerializer, UserSerializer
from usuarios.permissions import IsLoggedUserOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


class ProfileViewset(viewsets.ModelViewSet):
    """API endpoint that allows profiles to be viewed or edited"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, IsLoggedUserOrReadOnly)
