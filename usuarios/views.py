from .models import Profile
from rest_framework import viewsets
from usuarios.serializers import ProfileSerializer


class ProfileViewset(viewsets.ModelViewSet):
    """API endpoint that allows profiles to be viewed or edited"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
