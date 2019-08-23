#from django.contrib.auth.models import User
from core_auth.models import User
from .models import Profile
from rest_framework import serializers
from grupos.models import Pedal, Grupo
from grupos.serializers import GrupoSerializer
from django.contrib.auth.password_validation import validate_password


class PedalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedal
        fields = (
            'id',
            'url',
            'nome_ou_destino',
            'distancia',
            'nivel',
            'terreno',
            'info',
            'pago',
            'preco',
            'grupo',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    pedais = PedalSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('url', 'user',
                  'tel_emergencia',
                  'is_grupo_admin', 'pedais', )
