from .models import Grupo, Pedal
from rest_framework import serializers
from usuarios.models import Profile
from django.contrib.auth.models import User


class PedalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pedal
        fields = ('id',
                  'url',
                  'nome_ou_destino',
                  'distancia',
                  'nivel',
                  'terreno',
                  'info',
                  'pago',
                  'preco',
                  'grupo',
                  'participantes'
                  )


class AdminGrupoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField(source='user.id')

    class Meta:
        model = Profile
        fields = ('url', 'id',)


class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    pedais = PedalSerializer(many=True, read_only=True)
    admin = AdminGrupoSerializer(read_only=True)

    class Meta:
        model = Grupo
        fields = ('url', 'id', 'admin', 'nome', 'logo', 'pedais')


class PedalReadOnlylSerializer(serializers.ModelSerializer):

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
        read_only_fields = ('__all__',)


class GrupoReadOnlySerializer(serializers.ModelSerializer):
    pedais = PedalReadOnlylSerializer(many=True, read_only=True)
    #admin = AdminGrupoSerializer(read_only=True)

    class Meta:
        model = Grupo
        fields = (
            "url",
            "id",
            "nome",
            "logo",
            # "admin",
            "pedais")
        read_only_fields = ('__all__', )
