# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compagnie',
            name='nom',
            field=models.CharField(default='Entrez un nom', max_length=50, verbose_name='Nom'),
        ),
    ]
