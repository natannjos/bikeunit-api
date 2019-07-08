from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class Grupo(models.Model):

    nome = models.CharField('Nome', max_length=50)
    logo = models.URLField('Logo', blank=True, null=True)
    admin = models.ForeignKey(
        'usuarios.Profile', verbose_name="Admin", on_delete=models.CASCADE, limit_choices_to={'is_grupo_admin': True}, related_name='grupos')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ('created', )


class Pedal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome_ou_destino = models.CharField('Nome ou Destino', max_length=50)
    distancia = models.DecimalField(
        'Distância', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    nivel = models.CharField(
        'Nível',
        max_length=1,
        choices=(
            ('1', 'Iniciante'),
            ('2', 'Médio'),
            ('3', 'Avançado'),
        ))
    terreno = models.CharField(
        'Tipo de Terreno',
        max_length=1,
        choices=(
            ('1', 'Terra'),
            ('2', 'Asfalto'),
            ('3', 'Misto'),
        ))
    info = models.TextField("Informações Adicionais", blank=True, null=True)
    pago = models.BooleanField("Pedal pago?", default=False)
    preco = models.DecimalField(
        'Preço', max_digits=10,
        decimal_places=2, validators=[MinValueValidator(0)],
        blank=True, null=True
    )
    grupo = models.ForeignKey("grupos.Grupo", verbose_name="Grupo",
                              on_delete=models.CASCADE, related_name='pedais')
    participantes = models.ManyToManyField(
        "usuarios.Profile", verbose_name="Lista de Participantes",
        blank=True, related_name='pedais'
    )

    def __str__(self):
        return self.destino

    class Meta:
        verbose_name = 'Pedal'
        verbose_name_plural = 'Pedais'
        ordering = ('created', )
