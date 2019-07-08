from django.contrib.auth.models import User
from .models import Profile
from rest_framework import serializers
from grupos.models import Pedal, Grupo
from grupos.serializers import GrupoSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class PedalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pedal
        fields = ('url',
                  'destino',
                  'distancia',
                  'nivel',
                  'terreno',
                  'info',
                  'pago',
                  'preco',
                  'grupo')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)
    pedais = PedalSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('url',
                  'user',
                  'pedais',
                  'tel_emergencia',
                  'is_grupo_admin',
                  'meu_grupo')
