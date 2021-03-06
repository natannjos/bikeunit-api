# Generated by Django 2.2.1 on 2019-07-30 01:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel_emergencia', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[0-9]*$')], verbose_name='Tel de Emergência')),
                ('is_grupo_admin', models.BooleanField(default=False, verbose_name='É Admin de grupo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
