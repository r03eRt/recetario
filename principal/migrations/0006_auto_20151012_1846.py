# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.TextField(verbose_name='comentario', help_text='comentario'),
        ),
    ]
