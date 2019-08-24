#from django.contrib.auth.models import User
from core_auth.models import User
from .models import Profile
from rest_framework import serializers
from grupos.models import Pedal, Grupo
from grupos.serializers import GrupoSerializer
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    pedais = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Pedal.objects.all())

    class Meta:
        model = Profile
        fields = ('url', 'user',
                  'tel_emergencia',
                  'is_grupo_admin', 'pedais', )
