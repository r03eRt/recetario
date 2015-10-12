# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_auto_20151012_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(upload_to='photo/', verbose_name='Imagen'),
        ),
    ]
