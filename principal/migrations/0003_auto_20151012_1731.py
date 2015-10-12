# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_receta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Receta',
        ),
    ]
