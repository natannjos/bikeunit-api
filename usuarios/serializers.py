from django.contrib.auth.models import User
from .models import Profile
from rest_framework import serializers
from grupos.models import Pedal, Grupo
from grupos.serializers import GrupoSerializer
from django.contrib.auth.password_validation import validate_password


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    pedais = PedalSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('url', 'user',
                  'tel_emergencia',
                  'is_grupo_admin', 'pedais', )


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    # def validate_new_password(self, value):
    #    validate_password(value)
    #    return value
