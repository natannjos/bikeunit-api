from .models import Grupo, Pedal
from rest_framework import serializers
from usuarios.models import Profile
from django.contrib.auth.models import User


class PedalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pedal
        fields = '__all__'


class AdminGrupoSerializer(serializers.HyperlinkedModelSerializer):
    nome = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = ('url', 'nome',)


class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    pedais = PedalSerializer(many=True, read_only=True)
    admin = AdminGrupoSerializer(read_only=True)

    class Meta:
        model = Grupo
        fields = ('__all__')
