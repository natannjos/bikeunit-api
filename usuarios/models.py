from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel_emergencia = models.CharField(
        'Tel de Emergência', max_length=11, validators=[RegexValidator(r'^[0-9]*$')])
    is_grupo_admin = models.BooleanField("É Admin de grupo", default=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
