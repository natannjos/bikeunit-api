from .models import Grupo, Pedal
from rest_framework import serializers
from usuarios.models import Profile
from django.contrib.auth.models import User


class PedalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pedal
        fields = '__all__'


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class AdminGrupoSerializer(serializers.HyperlinkedModelSerializer):
    user = AdminUserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('url', 'user',)


class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    pedais = PedalSerializer(many=True, read_only=True)
    admin = AdminGrupoSerializer(required=True)

    class Meta:
        model = Grupo
        fields = ('__all__')
