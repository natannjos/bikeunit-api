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


class PedalProfileSerializer(serializers.HyperlinkedModelSerializer):
    nomeGrupo = serializers.CharField(source='grupo.nome', read_only=True)
    logoGrupo = serializers.CharField(source='grupo.logo', read_only=True)
    data = serializers.DateField(
        format="%d/%m/%Y", required=True)
    hora = serializers.TimeField(
        format="%H:%M", required=True)
    nivel = serializers.CharField(source='get_nivel_display')
    terreno = serializers.CharField(source='get_terreno_display')

    class Meta:
        model = Pedal
        fields = ('id',
                  'url',
                  'nome_ou_destino',
                  'data',
                  'hora',
                  'encontro',
                  'distancia',
                  'nivel',
                  'terreno',
                  'info',
                  'pago',
                  'preco',
                  'grupo',
                  'nomeGrupo',
                  'logoGrupo'
                  )
        read_only_fields = ('__all__',)


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    pedais = PedalProfileSerializer(
        many=True)

    class Meta:
        model = Profile
        fields = ('url', 'user',
                  'tel_emergencia',
                  'is_grupo_admin', 'pedais')
