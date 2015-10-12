# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('titulo', models.CharField(unique=True, max_length=100)),
                ('ingredientes', models.TextField(help_text='Redacta los ingredientes')),
                ('preparacion', models.TextField(verbose_name='Preparación')),
                ('imagen', models.ImageField(verbose_name='Imágen', upload_to='recetas')),
                ('tiempo_registro', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
