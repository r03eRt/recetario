# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_receta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('texto', models.TextField(help_text='Tu comentario', verbose_name='comentario')),
                ('receta', models.ForeignKey(to='principal.Receta')),
            ],
        ),
    ]
