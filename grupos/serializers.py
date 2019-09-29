from .models import Grupo, Pedal
from rest_framework import serializers
from usuarios.models import Profile
from django.contrib.auth.models import User


class PedalSerializer(serializers.HyperlinkedModelSerializer):
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
        fields = ('url', 'id', 'admin', 'nome', 'logo', 'membros', 'pedais')


class PedalReadOnlylSerializer(serializers.ModelSerializer):
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
        fields = (
            'id',
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


class GrupoReadOnlySerializer(serializers.ModelSerializer):
    pedais = PedalReadOnlylSerializer(many=True, read_only=True)
    # admin = AdminGrupoSerializer(read_only=True)

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


class EntrarESairDePedalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedal
        fields = ('id',
                  'url',
                  'grupo',
                  'participantes'
                  )
        read_only_fields = ('id',
                            'url',
                            'grupo',
                            )

    def only_logged_user_change(self, old_list, new_list):
        logged_profile = self.context['request'].user.profile
        diff = []
        # print(logged_profile)
        # remove
        if set(old_list) > set(new_list):
            diff = list(set(old_list) - set(new_list))
            print(diff)

        # added
        elif set(old_list) < set(new_list):
            diff = list(set(new_list) - set(old_list))

        if len(diff) == 0 or len(diff) == 1 and diff[0] == logged_profile:
            return True
        return False

    def update(self, instance, validated_data):
        old_list = list(instance.participantes.all())
        new_list = validated_data['participantes']
        if self.only_logged_user_change(old_list, new_list):
            instance.participantes.set(new_list)
            instance.save
        return instance
